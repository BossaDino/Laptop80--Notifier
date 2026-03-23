# PowerReader

PowerReader is a lightweight Python utility that monitors your Windows laptop's battery charging status. It runs quietly in the system tray and sends a Windows 11 toast notification when your battery reaches 80% while plugged in, helping you unplug in time to preserve your battery's long-term health.

## Features

* **Custom Notifications:** Uses native Windows 11 toast notifications with an "incoming call" scenario for high visibility.
* **System Tray Integration:** Runs in the background with a system tray icon, allowing you to easily exit the script at any time.
* **Smart Monitoring:** Automatically pauses monitoring when the laptop is unplugged to save resources.
* **Anti-Spam:** Limits notifications to prevent notification spamming while your device sits at or above 80%.

## Prerequisites

Before running the script, ensure you have Python 3 installed on your machine. You will also need to install the required external libraries.

Install the dependencies using `pip`:

```bash
pip install psutil win11toast pystray Pillow
