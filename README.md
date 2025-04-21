# Project-Lora
 a child-focused humanoid robot named Lora that listens and responds in a kid-like  voice using speech APIs, tracks user movement with ESP32-CAM for eye contact, and animates its limbs and  neck with servo motors for interactive engagement
# Project Lora – Child-Focused Humanoid Robot

Project Lora is an interactive humanoid robot designed for children, featuring natural speech interaction, computer vision-based eye contact, and expressive movements. The system combines ESP32-CAM for real-time face tracking, Arduino-controlled servo motors for limb and neck articulation, and cloud APIs for speech recognition and kid-like voice responses, creating an engaging and friendly companion for young users.

---

## Features

- **Speech Interaction:** Listens to children’s speech and responds using speech-to-text and text-to-speech APIs, imitating a young, friendly voice.
- **Vision-Based Eye Contact:** Uses ESP32-CAM and computer vision to track the user’s face and maintain eye contact.
- **Expressive Movements:** Animates limbs and neck with servo motors for lifelike gestures and engagement.
- **Multi-Controller Architecture:** Integrates ESP32-CAM for vision, Arduino for motion, and Python for AI and API orchestration.
- **Safe and Child-Friendly:** Designed with safety and approachability in mind, suitable for interactive learning and play.

---

## Tech Stack

- **Hardware:** ESP32-CAM, Arduino Uno, SG90 Servo Motors, PCA9685 Servo Driver, Microphone Module, Speaker/Audio Output
- **Software:** Python (OpenCV, sounddevice, edge-tts, requests, dotenv, pyserial), Arduino IDE (Servo library), ESP32Servo library
- **APIs:** Deepgram (Speech-to-Text), Edge-TTS (Text-to-Speech), OpenRouter (Conversational AI)
- **Communication:** UART Serial between controllers

---

## System Overview

1. **Speech Input:** Child speaks, audio is recorded and transcribed via speech-to-text API.
2. **AI Response:** Transcribed text is sent to a conversational AI model; a friendly, age-appropriate response is generated.
3. **Voice Output:** Response is converted to speech using a kid-like voice and played through the robot.
4. **Face Tracking:** ESP32-CAM detects and tracks the user’s face, adjusting head/eye position to maintain eye contact.
5. **Motion Control:** Arduino receives animation commands (e.g., wave, nod, dance) via serial and actuates servo motors for expressive movement.

---

## Setup Instructions

1. **Hardware Assembly:**
   - Connect servo motors to the Arduino or PCA9685 driver.
   - Wire ESP32-CAM for face tracking and UART communication.
   - Connect microphone and speaker to the main controller.
   - Ensure safe power supply (e.g., regulated 5V for servos and controllers).

2. **Software Installation:**
   - Install Arduino IDE and required libraries (`Servo`, `ESP32Servo`).
   - Flash ESP32-CAM and Arduino with provided firmware.
   - Install Python 3.x and dependencies:
     ```
     pip install opencv-python sounddevice scipy edge-tts requests python-dotenv pyserial
     ```
   - Set up `.env` file with API keys for Deepgram, Edge-TTS/ElevenLabs, and OpenRouter/OpenAI.

3. **Running the Project:**
   - Power on all hardware components.
   - Run the Python control script:
     ```
     python lora_controller.py
     ```
   - Interact with Lora by speaking; the robot will respond, track your face, and animate accordingly.

---

## Circuit and Wiring

- **ESP32-CAM:** Connects to pan/tilt servos for head movement and communicates with Arduino via UART.
- **Arduino:** Controls limb servos and receives animation commands from Python script.
- **Microphone/Speaker:** Connected to main controller for audio input/output.

---

## Contribution

Contributions and suggestions are welcome! Please open an issue or pull request on the repository.


