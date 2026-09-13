import os 
import pyautogui
import webbrowser
import pyttsx3
from time import sleep

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


dictapp ={"commanndprompt":"cmd","microsoft store":"microsoft store","calculator":"calc","camera":"start microsoft.windows.camera:","vlc media player":"vlc" "winword","excel":"excel","power point":"powerpnt","spotify":"spotify","chrome":"chrome","firefox":"firefox"," edge":"msedge","notepad":"notepad","wordpad":"write","paint":"mspaint","snipping tool":"snippingtool","task manager":"taskmgr","control panel":"control","file explorer":"explorer","settings":"ms-settings:","microsoft word":"microsoft word","teams":"teams","YouTube":"YouTube"}

def openappweb(query):
    speak("launching, sir")
    if " .com" in query or ".co.in" in query or ".org" in query:
        query = query.replace("open","")
        queery = query.replace("jarvis","")
        query = queery.replace("launch","")
        query = query.replace(" ","")
        webbrowser.open(f"https://www.{query}")
    else:
        keys =  list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"start {dictapp[app]}")

def closeappweb(query):
    speak("closing, sir")
    if "one tab " in query or "1 tab" in query:
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed, sir")

    elif "2 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed, sir")

    elif "3 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed, sir")

    elif "4 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        speak("all tabs closed, sir")

    elif "5 tab" in query:
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        pyautogui.hotkey("ctrl","w")
        sleep(0.5)
        speak("all tabs closed, sir")


    else:
        keys =  list(dictapp.keys())
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")
                
                    