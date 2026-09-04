<div align="center">

# 🚀 Astrobyte WOL

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
  astrobyte-wol:
    image: moon132/astrobyte_wol:latest
    container_name: astrobyte-wol
    network_mode: host
    volumes:
      - ./data:/app/data
    restart: unless-stopped


## 🌐 Accessing the Dashboard

Once the container is running, open your favorite web browser and enter the IP address of your Docker host followed by port 5000:

**`http://<YOUR-SERVER-IP>:5000`**

*(Example: `http://192.168.1.100:5000`)*