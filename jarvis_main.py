import datetime
import pyttsx3
import speech_recognition 
import requests
from bs4 import BeautifulSoup
import pyautogui 
import os
from plyer import notification
from pygame import mixer
import speedtest
import requests
import asyncio 
import asyncio 
import edge_tts
import pygame
import threading



for i in range(3):
    a = input("enter password to open jarvis :- ")
    pw_file = open("password.txt", "r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("WELCOME SIR ! PLZ SPEAK[WAKE UP] TO LOAD ME UP")
        break
    elif(i==2 and a!= pw):
        exit()
    elif(a!=pw):
        print("Try again")

from INTRO import play_gif
play_gif


engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        audio = r.listen(source,0,4)
    try:
        print("understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print("say that again please...")
        return "None"
    return query

# def alarm(query):
#     timehere =open("Alarmstext.txt","a")
#     timehere.write(query)
#     timehere.close()
#     # os.startfile("jarvis_main.py")    



if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        if "wake up" in query:
            from GreetMe import greetMe
            greetMe()

            while True:
                query = takeCommand().lower()
                if "go to sleep" in query:
                    speak("ok sir, you can call me anytime")
                    break

               ###########JARVIS the trilogy 2.0###################

                elif "change password" in query:
                    speak ("what is the new password")
                    new_pw = input("Enter the new password\n")
                    new_password = open("password.txt","w")
                    new_password.write(new_pw)
                    new_password.close()
                    speak("Done sir")
                    speak(f"your newe pasword is{new_pw}")

                elif "schedule my day" in query:
                    tasks = [] #empty list
                    speak("do you want  to clear old task(PLZ speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("tasks.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks  = int(input("Enter the no of tasks:- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}.{tasks[i]}/n")
                            file.close()

                    elif "no" in query:
                        i = 1
                        no_tasks  = int(input("Enter the no of tasks:- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the tasks :- "))
                            file = open("tasks.txt", "a")
                            file.write(f"{i}.{tasks[i]}/n")
                            file.close()
                elif "show my schedule" in query:                
                    file = open("tasks.txt","r")
                    content = file.read()
                    file.close()
                    mixer.init()
                    mixer.music.load("notification.mp3")
                    mixer.music.play()
                


                    
                    notification.notify(
                        tittle = "My schedule :-",
                        message = content,
                        timeout = 15
                    )
                
                
                    
                elif "open" in query:
                    query = query.replace("open", "")
                    query = query.replace("Jarvis","")
                    pyautogui.press("super")
                    pyautogui.typewrite(query)
                    pyautogui.sleep(2)
                    pyautogui.press("enter")


                elif "internet speed" in query:
                    wifi = speedtest.Speedtest()
                    upload_net = wifi.upload()/10485756     #1 Mega bytes = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Wifi upload speed is ", upload_net)
                    print("Wifi download speed is ",download_net)
                    speak(f"Wifi download speed is{download_net}")
                    speak(f"Wifi upload speed is{upload_net}")                    

                
                elif "ipl score" in query:
                    from plyer import notification   #pip install plyer
                    import requests   #pip install requests
                    from bs4 import BeautifulSoup  #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ ="cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n  {team2} : {team2_score}",
                        timeout = 10
                    )



                elif "play game" in query:
                    from game import game_paly
                    game_paly()

                
                 
                   
                    



               
                     





                



            ##############################################################


               
                elif "hello" in query:
                    speak("hello sir, how are you?")
                elif "i am good"  in query:
                    speak("that's great sir")
                elif "how are you" in query:
                    speak("perfect sir")
                elif "thank you" in query:
                    speak("your welcome sir")


                elif "pause" in query:
                    pyautogui.press("k") 
                    speak("video paused") 
                elif "play" in query:
                    pyautogui.press("k") 
                    speak("video played") 
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted") 
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("turningk volume up, sir")
                    volumeup()
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("turning volume down, sir")
                    volumedown()    



                elif "open" in query:
                    from Dictapp import openappweb
                    openappweb(query)
                elif "close" in query:
                    from Dictapp import closeappweb
                    closeappweb(query)


                elif "google" in query:
                    from SearchNow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from SearchNow import searchYouTube
                    searchYouTube(query)
                elif "wikipedia" in query:
                    from SearchNow import searchWikipedia
                    searchWikipedia(query)


                elif "calculate" in query:
                    from Calculator_number import wolframalpha
                    from Calculator_number import Calc
                    query = query.replace("calculate","")
                    query = query.replace("jarvis","")
                    Calc(query)

                elif "whatsapp" in query:
                    from Whatsapp import sendMessage
                    sendMessage()
                
                
                elif "temperature" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")
                elif "weather" in query:
                    search = "temperature in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current {search} is {temp}")

                # elif "set an alarm " in query:
                #     print("input time example:- 10 and 10 and 10")
                #     speak("set the time")
                #     a = input("please tell the time:- ")
                #     alarm(a)
                #     speak("done sir")

                elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M:")
                    speak(f"sir, the time is {strTime}")

                elif "finally sleep" in query:
                    speak("ok sir, you can call me anytime")
                    exit()
                    
                elif "remember that" in query:
                    remembermessage = query.replace("remember that", "")
                    remembermessage = query.replace("jarvis", "")
                    speak("you told me to remember that" + remembermessage)
                    remember = open("remember.txt", "w")
                    remember.write(remembermessage)
                    remember.close()
                elif "what do you remember" in query:
                    remember = open("remember.txt", "r")
                    speak("you told me to remember that" + remember.read())

                elif "shutdown system" in query:
                    speak("Are you sure you want to shutdown")
                    shutdown = input("do you wish to shutdown your coumpter ? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")
                    elif shutdown == "no":
                        break
                      
                elif "restart system" in query:
                    speak("Are you sure you want to Restart your System")
                    Restart = input("do you wish to Restart your coumpter ? (yes/no)")
                    if Restart == "yes":
                        os.system("shutdown /r /t 1")
                    elif Restart == "no":
                        break
               
                