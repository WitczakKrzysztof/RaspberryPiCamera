# Raspberry Pi Camera UART Transmission

## 📌 Project Overview
This project demonstrates how to use a **Raspberry Pi** with a **camera module** to capture images or videos and transmit them to a **PC** via **UART communication**.  
It provides a lightweight and efficient way to transfer media between a Raspberry Pi and a host computer without requiring high-level network protocols.

---

## 🛠️ Hardware Requirements
- Raspberry Pi (any model with UART support)
- Raspberry Pi Camera Module (CSI or USB-based)
- PC with a UART interface (or USB-to-UART adapter)
- Jumper wires (TX, RX, GND connections)

---

## ⚙️ Software Requirements
- Raspberry Pi OS (Lite or Desktop)
- Python 3
- `picamera2` or `libcamera` (for camera control, depending on OS version)
- `pyserial` (for UART communication)
- Serial terminal software on PC (e.g., `minicom`, `PuTTY`, or a Python script with `pyserial`)

---

## 🔌 Wiring Setup
1. Connect **Raspberry Pi TX → PC RX**  
2. Connect **Raspberry Pi RX → PC TX**  
3. Connect **GND → GND**  

⚠️ **Important**: Ensure voltage levels are compatible (Raspberry Pi UART uses **3.3V** logic). Use a level shifter if required.

---

## 🚀 How It Works
1. The Raspberry Pi initializes the camera module.  
2. The user captures an image or video.  
3. The captured media is serialized (converted into bytes).  
4. Data is transmitted via UART to the PC.  
5. The PC receives and reconstructs the file.  

---

## 📂 Project Structure
