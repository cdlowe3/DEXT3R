import os
import pyttsx3

sec=30

os.system(f'shutdown /r /t {sec}')

pyttsx3.speak(f'Ok I am rebooting your PC in the next {sec} seconds')