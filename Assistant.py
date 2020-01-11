import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your Personal Assistant. Please tell me, How may I help you?")


def takeCommand():
    # it takes microphone input from the user and return string
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        querys = r.recognize_google(audio, language='en-us')
        print("User said:", querys)

    except Exception as e:
        print("Say That again!")
        return "None"
    return querys


def show_result(response):
    print(response)
    speak(response)


def browser_open(url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


def Action_Perform(query):
    if 'wikipedia' in query:
        show_result('Searching Wikipedia...')
        query = query.replace('wikipedia', '')
        result = wikipedia.summary(query, sentences=2)
        show_result('According to wikipedia:')
        show_result(result)
    elif 'youtube' in query:
        query = query.replace('youtube', '')
        show_result('Search youtube...')
        browser_open('https://www.youtube.com/results?search_query='+query)
    elif 'stackoverflow' in query:
        query = query.replace('stackoverflow', '')
        show_result('search stackoverflow...')
        browser_open('https://stackoverflow.com/search?q='+query)
    elif 'open facebook' in query:
        show_result('Opening Facebook')
        browser_open('www.facebook.com')
    elif 'google' in query:
        query = query.replace('google', '')
        show_result('Searching Google...')
        browser_open('https://www.google.com/search?q='+query)
    elif 'play music' in query:
        music_dir = "D:\\Shahid"
        songs = os.listdir(music_dir)
        show_result("Opening music...")
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'play video' in query:
        music_dir = "F:\\Download"
        songs = os.listdir(music_dir)
        show_result("Opening Video...")
        os.startfile(os.path.join(music_dir, songs[0]))
    elif 'show time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
        show_result(strTime)
    elif 'who are you' in query:
        show_result('I am Siri. I am your Personal Assistant. You are my inventor,Sir. Thank You')
    elif 'open torrent' in query:
        # Opening Specific Software
        path = "C:\\Program Files\\qBittorrent\\qbittorrent.exe"
        os.startfile(path)
    elif 'thank' or 'thanks' or 'thank you' in query:
        show_result('Welcome. Sir')


if __name__ == '__main__':
    speak("Hello,Sir.")
    # wishMe()

    # task which command execute
    while 1:
        query = takeCommand().lower()
        if 'terminate' in query:
            show_result("Terminating sir...")
            break
        else:
            Action_Perform(query)




