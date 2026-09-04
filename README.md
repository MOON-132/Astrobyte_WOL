<div align="center">

# 🚀 Modern WOL Dashboard

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![React](https://img.shields.io/badge/react-%2320232a.svg?style=for-the-badge&logo=react&logoColor=%2361DAFB)
![TailwindCSS](https://img.shields.io/badge/tailwindcss-%2338B2AC.svg?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

A lightweight, modern, and fully responsive Wake-on-LAN (WOL) dashboard built with Python (Flask), React, and Tailwind CSS.

> 🖼️ **Note:** Add a screenshot of your dashboard here! (e.g., `![Dashboard](docs/screenshot.png)`)

</div>

---

## ✨ Features

- **Modern UI:** Built with React and Tailwind CSS, featuring glassmorphism and smooth animations.
- **Live Status:** Automatically pings your devices in the background to show real-time online/offline status.
- **Customizable:** Change the app title, upload a custom logo via URL, and choose your favorite accent color.
- **Dark/Light Mode:** Fully supported and saved in your settings.
- **Persistent Data:** Devices and settings are saved locally in a JSON file via Docker volumes.
- **Network Ready:** Uses host networking to successfully broadcast Magic Packets (WOL) across your local network.

## 🐳 Quick Start (Using Pre-built Docker Image)

The easiest way to deploy the dashboard is using the pre-built image from Docker Hub. 

1. Create a `docker-compose.yml` file:

```yaml
version: '3.8'

services:
  wol-dashboard:
    image: dein-dockerhub-name/wol-dashboard:latest
    container_name: wol-dashboard
    network_mode: host
    volumes:
      - ./data:/app/data
    restart: unless-stopped
```

2. Start the container:
```bash
docker-compose up -d
```

3. Open your browser and navigate to `http://<YOUR-SERVER-IP>:5000`

> ⚠️ **Note on `network_mode: host`:** This is usually required for Wake-on-LAN magic packets to be successfully broadcasted to your physical network. Because of this, standard port mapping (`ports: - "5000:5000"`) is ignored, and the app will be accessible directly on port 5000 of your host machine.

## 🛠️ Manual Build (For Developers)

If you want to build the image yourself from the source code:

1. Clone this repository:
```bash
git clone https://github.com/DEIN_GITHUB_NAME/modern-wol-dashboard.git
cd modern-wol-dashboard
```

2. Run the build command:
```bash
docker-compose up -d --build
```

## 📂 Folder Structure (Data)

The container creates a `data` folder mapped to `/app/data` inside the container. This folder contains:
- `computers.json`: Stores your added PCs (Name, IP, MAC).
- `settings.json`: Stores your dashboard settings (Theme, Title, Logo, Color).
