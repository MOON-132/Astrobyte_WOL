import os
import json
import subprocess
import threading
import time
from flask import Flask, render_template, request, jsonify
from wakeonlan import send_magic_packet

app = Flask(__name__)

# Pfade für dauerhafte Datenspeicherung
DATA_DIR = 'data'
COMPUTERS_FILE = os.path.join(DATA_DIR, 'computers.json')
SETTINGS_FILE = os.path.join(DATA_DIR, 'settings.json')

# Erstelle den Ordner, falls er nicht existiert
os.makedirs(DATA_DIR, exist_ok=True)

# Cache für den Live-Status der PCs
status_cache = {}

def load_json(filepath, default):
    if not os.path.exists(filepath):
        return default
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except Exception:
        return default

def save_json(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=4)

# Hintergrund-Thread: Pingt alle PCs alle 10 Sekunden an
def ping_loop():
    while True:
        comps = load_json(COMPUTERS_FILE, [])
        for c in comps:
            ip = c.get('ip')
            if ip:
                # -c 1 (1 Paket), -W 1 (1 Sekunde Timeout)
                res = subprocess.run(
                    ['ping', '-c', '1', '-W', '1', ip], 
                    stdout=subprocess.DEVNULL, 
                    stderr=subprocess.DEVNULL
                )
                status_cache[c['id']] = 'online' if res.returncode == 0 else 'offline'
        time.sleep(10)

threading.Thread(target=ping_loop, daemon=True).start()

# --- Routen ---

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/settings', methods=['GET', 'POST'])
def manage_settings():
    if request.method == 'POST':
        save_json(SETTINGS_FILE, request.json)
        return jsonify({"status": "success"})
    
    default_settings = {"title": "WOL Dashboard", "logoUrl": "", "theme": "dark", "accent": "blue"}
    return jsonify(load_json(SETTINGS_FILE, default_settings))

@app.route('/api/computers', methods=['GET', 'POST'])
def manage_computers():
    if request.method == 'POST':
        save_json(COMPUTERS_FILE, request.json)
        return jsonify({"status": "success"})
    
    comps = load_json(COMPUTERS_FILE, [])
    for c in comps:
        # Lese Status aus dem Thread-Cache
        c['status'] = status_cache.get(c['id'], 'offline')
    return jsonify(comps)

@app.route('/api/wake', methods=['POST'])
def wake():
    mac = request.json.get('mac')
    if mac:
        send_magic_packet(mac)
        return jsonify({"status": "success", "message": "Magic Packet gesendet!"})
    return jsonify({"status": "error", "message": "Keine MAC-Adresse angegeben"}), 400

if __name__ == '__main__':
    # Flask auf Port 5000 starten
    app.run(host='0.0.0.0', port=5000)