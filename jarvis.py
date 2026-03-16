import sounddevice as sd
import numpy as np
import os
import time
import subprocess
# Version 1.2
# -------------------------
# SETTINGS
# -------------------------
THRESHOLD = 0.7   # Adjust if needed
COOLDOWN = 4      # Seconds between triggers

last_trigger_time = 0

# -------------------------
# OPEN PRODUCTIVITY SETUP
# -------------------------
def open_apps():
    print("🟢 Clap detected! Launching JARVIS mode...")

    # Open Apps
    subprocess.run(["open", "-a", "Google Chrome"])
    subprocess.run(["open", "-a", "Spotify"])
    subprocess.run(["open", "-a", "Visual Studio Code"])

    time.sleep(3)

    # Open specific Chrome tabs
    subprocess.run(["open", "-a", "Google Chrome", "https://mail.google.com"])
    subprocess.run(["open", "-a", "Google Chrome", "https://chat.openai.com"])
    subprocess.run(["open", "-a", "Google Chrome", "https://github.com"])

# -------------------------
# CLAP DETECTION LOGIC
# -------------------------
def audio_callback(indata, frames, time_info, status):
    global last_trigger_time

    volume_norm = np.linalg.norm(indata)

    current_time = time.time()

    if volume_norm > THRESHOLD and (current_time - last_trigger_time) > COOLDOWN:
        last_trigger_time = current_time
        open_apps()

# -------------------------
# START LISTENING
# -------------------------
def listen():
    print("🎤 Listening for clap...")
    with sd.InputStream(callback=audio_callback):
        while True:
            time.sleep(0.1)

if __name__ == "__main__":
    listen()