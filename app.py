import os
import sounddevice as sd
import scipy.io.wavfile as wav
import requests
from dotenv import load_dotenv
import time
import json
import serial
from serial.tools import list_ports
import asyncio
import edge_tts
import pygame
import tempfile

# Initialize components
load_dotenv()
pygame.mixer.init()

class LoraController:
    def __init__(self):
        self.robot_serial = self.init_serial()
        self.session_memory = []
        self.setup_apis()

    def init_serial(self):
        try:
            ports = list_ports.comports()
            for port in ports:
                if "USB" in port.description:
                    return serial.Serial(port.device, 115200, timeout=1)
            raise Exception("Robot not connected!")
        except Exception as e:
            print(f"Serial Error: {e}")
            return None

    def setup_apis(self):
        self.dg_key = os.getenv("DEEPGRAM_API_KEY")
        self.or_key = os.getenv("OPENROUTER_API_KEY")
        self.model = "google/gemini-flash-1.5-8b-exp"

    def speak(self, text):
        print(f"Lora: {text}")
        asyncio.run(self.edge_tts_speak(text))
        if self.robot_serial:
            self.trigger_animation('speak')

    async def edge_tts_speak(self, text):
        try:
            communicate = edge_tts.Communicate(
                text=text,
                voice="en-US-AnaNeural",
                pitch="+10Hz",
                rate="-10%"
            )
            
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as f:
                temp_path = f.name
                async for chunk in communicate.stream():
                    if chunk["type"] == "audio":
                        f.write(chunk["data"])
                        
            pygame.mixer.music.load(temp_path)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
                
            os.remove(temp_path)
        except Exception as e:
            print(f"TTS Error: {e}")

    def trigger_animation(self, anim_type):
        cmd = {'happy': 'H', 'wave': 'W', 'speak': 'S'}.get(anim_type, 'N')
        self.robot_serial.write(f"{cmd}\n".encode())

    def process_command(self, command):
        if "hello" in command.lower():
            self.trigger_animation('wave')
        elif "happy" in command.lower():
            self.trigger_animation('happy')
        return self.get_ai_response(command)

    def get_ai_response(self, prompt):
        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.or_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": self.model,
                    "messages": [{
                        "role": "user",
                        "content": f"Respond as Lora: {prompt}"
                    }]
                }
            )
            return response.json()['choices'][0]['message']['content']
        except Exception as e:
            print(f"AI Error: {e}")
            return "Let's try that again!"

if __name__ == "__main__":
    lora = LoraController()
    lora.speak("Hi! I'm Lora, your new friend!")
    
    while True:
        print("Listening...")
        filename = "recording.wav"
        fs = 44100
        duration = 5
        
        recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
        sd.wait()
        wav.write(filename, fs, recording)
        
        text = lora.transcribe_audio(filename)
        if text:
            response = lora.process_command(text)
            lora.speak(response)
