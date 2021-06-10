# Import Statements
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import sys
from datetime import date
import pyjokes
import pyautogui
import speedtest

# Selecting Voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

# Web Browser Paths
# MacOS
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'

# Windows
chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'

# Linux
# chrome_path = '/usr/bin/google-chrome %s'

# Speak Function Which Takes Audio As input


def speak(audio):
    """
    A Function That Lets Jarvis Speak
    """
    engine.say(audio)
    engine.runAndWait()

# wishMe Function


def wishMe():
    """
    Wishes With Correct Greeting According To Time Whenever The Program Starts
    """
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis Sir. Plese tell me how may I help you")

# takeCommand Function


def takeCommand():
    """
    Takes Commands From The User Using Microphone & Returns Str. Output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # Using google for voice recognition.
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")  # User query will be printed.

    except Exception as e:
        # print(e)
        # Say that again will be printed in case of improper voice
        print(f"{e}, Say that again please...")
        return "None"  # None string will be returned
    return query

# joke function


def joking():
    """
    Jarvis will speak a joke with this function
    """
    joke = pyjokes.get_joke('en', category='neutral')
    print(joke)
    speak(joke)


# Main Function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic For Excecuting Tasks On Query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get(chrome_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chrome_path).open("google.com")

        elif 'open w schools' in query:
            webbrowser.get(chrome_path).open("w3schools.com")

        elif 'open classroom' in query:
            webbrowser.get(chrome_path).open("classroom.google.com")

        elif 'open school pad' in query:
            webbrowser.get(chrome_path).open("bhavansbaroda.schoolpad.in")

        elif 'open stack overflow' in query:
            webbrowser.get(chrome_path).open("stackoverflow.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'date' in query:
            strDate = date.today()
            speak(f"Sir, the date is {strDate}")

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "who are you" in query:
            speak("I am your personal desktop assistant Jarvis, sir")

        elif "who made you" in query:
            speak("Kuldeep Bhurani has created me")

        elif "what are you made of" in query:
            speak("Sir, I am made of a bunch of cool python code")

        elif "what can you do" in query:
            speak("I can do everything that you program in me, sir")

        elif 'how are you' in query:
            speak("I am fine sir, tell me about yourself")

        elif 'i am good' in query:
            speak("That's glad to hear sir")

        elif 'i am also fine' in query:
            speak("That's glad to hear sir")

        elif 'i am ok' in query:
            speak("Ok sir, good to hear that you are ok")

        elif 'not good' in query:
            speak("Ok sir, take care")

        elif 'open our youtube channel' in query:
            webbrowser.get(chrome_path).open(
                "https://www.youtube.com/channel/UCWv8I654A2w0ZJWNuDt42pg")

        elif 'hello' in query:
            speak("Hello sir, You can ask me do stuff and I will try to fullfill it")

        elif 'thank you' in query:
            speak("It's my pleasure sir")

        elif 'joke' in query:
            joking()

        elif 'volume up' in query:
            pyautogui.press('volumeup')
            speak("volume increased, sir")

        elif 'volume down' in query:
            pyautogui.press('volumedown')
            speak("volume decreased, sir")

        elif 'volume mute' in query:
            pyautogui.press('volumemute')

        elif 'volume unmute' in query:
            pyautogui.press('volumemute')
            speak("volume unmuted, sir")

        elif 'search youtube for' in query:
            speak("Searching YouTube...")
            print("Searching YouTube...")
            query = query.replace("search youtube for", "")
            webbrowser.get(chrome_path).open(
                f"https://www.youtube.com/results?search_query={query}")

        elif 'search google for' in query:
            speak("Searching Google...")
            print("Searching Google...")
            query = query.replace("search google for", "")
            webbrowser.get(chrome_path).open(
                f"https://www.google.com/search?q={query}")

        elif 'internet speed test' in query:
            st = speedtest.Speedtest()
            dl = st.download()
            up = st.upload()
            speak(
                f"sir at this time we have {up} upload speed and {dl} download speed, note that: intiger before point is the most important")
            print(
                f"sir at this time we have {up} upload speed and {dl} download speed, note that: intiger before point is the most important")

        elif 'bye' in query:
            print("Bye Sir! You can say quit to exit the program")
            speak("Bye Sir! You can say quit to exit the program")

        elif 'quit' in query:
            print("Bye Sir! Thank you for your time")
            speak("Bye Sir! Thank you for your time")
            sys.exit()

        else:
            speak(
                "Sir I cannot do that, if you want me to do thet you can program me further")
