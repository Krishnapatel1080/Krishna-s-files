import os
import eel
import time
import sys

from engine.features import *
from engine.command import *
from engine.auth import recoganize

    
eel.init("www")

playAssistantSound()
@eel.expose
def init():
    subprocess.call([r'device.bat'])
    eel.hideLoader()
    speak("Ready for Identification")
    time.sleep(3)
    flag = 1
    if flag == 1:

        vflag = 2   # Must be 1 after verifiction is created
        if vflag == 1:
            eel.init("www")
            os.system('start chrome.exe --app="http://localhost:8080/verify.html"')
            eel.start('verify.html', mode=None, host='localhost', block=True, size=(50,100))
            sys.exit()
        elif vflag <= 1:
            speak("Identifiction Fail")

        eel.hideFaceAuth()
        speak("Identification Successful")
        eel.hideFaceAuthSuccess()
        speak("Hello, I am Khushi, Your Personal Virtual Assistant")
        eel.hideStart()
        playAssistantSound()
        speak("I am ready to help you")
        
os.system('start chrome.exe --app="http://localhost:8000/index.html"')

eel.start('index.html', mode=None, host='localhost', block=True)