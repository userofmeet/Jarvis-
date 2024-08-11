import pyttsx3
import speech_recognition 
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)


#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


#convert voice into text 
def takecommand():
    r=speech_recognition.Recognizer()

    with speech_recognition.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout = 1, phrase_time_limit = 5)
        
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language = 'en-in')
        print(f"user said: {query}")
    
    except Exception as e:
        speak("Can you pls repeat...")
        return "none"

    return query 


def wish():
    hour = int(datetime.datetime.now().hour)
    
    if hour >= 0 and hour <= 12:
        speak("good morning")
    elif hour >= 12 and hour <= 18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("How can i help you sir")
    
    
if __name__ == "__main__":
    wish()
    #while True:
    if 1:
        query = takecommand().lower()
        if "open notepad" in query:
#npath = notepad file location 
            npath = "C:\\Program Files\\WindowsApps\\Microsoft.WindowsNotepad_11.2401.26.0_x64__8wekyb3d8bbwe\\Notepad\\notepad.exe"
            os.startfile(npath)
    
        # elif "open mission planner" in query:
        #     apath = "C:\\Users\\djain\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Mission Planner\\MissionPlanner-1.3.68.msi"
        #     os.startfile(apath)
          
        elif "open command prompt" in query:
            os.system("Start cmd")
            
        elif "open camera" in query:
            #0 for interal camera and 1 or port number for external camera
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k == 27:
                    break;
            cap.release()
            cv2.destroyAllWindows()
            
        elif "ip address" in query:
            #from requests
            ip = get('https://api.ipify.org').text
            speak(f"your IP address is {ip}")
            
        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
         
        elif "open google" in query:
            speak("sir what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
        
        elif "send message" in query:
            kit.sendwhatmsg("+919998760465","this is testing protocol",2,26)
        
