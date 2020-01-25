import datetime
import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import os
import psutil

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
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


def exit_app(msg):
    show_result(msg)
    exit(0)


def browser_open(url):
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)


def Action_Perform(query):
    if 'wikipedia' in query:
        show_result('Searching Wikipedia...')
        query = query.replace('wikipedia', '')
        result = wikipedia.summary(query, sentences=10)
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
        show_result('Enjoy Music Sir...')
    elif 'play video' in query:
        music_dir = "F:\\Download"
        songs = os.listdir(music_dir)
        show_result("Opening Video...")
        os.startfile(os.path.join(music_dir, songs[0]))
        show_result('Enjoy Video Sir...')
    elif 'kill video' in query:
        for process in (process for process in psutil.process_iter() if process.name() == "PotPlayerMini64.exe"):
            process.kill()
            show_result('Killing Video, Sir')
    elif 'show time' in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
        show_result(strTime)
    elif 'who are you' in query:
        show_result('I am Siri. I am your Personal Assistant. You are my inventor,Sir. Thank You')
    elif 'open torrent' in query:
        # Opening Specific Software
        path = "C:\\Program Files\\qBittorrent\\qbittorrent.exe"
        os.startfile(path)
        show_result('Opening qBittorent, Sir')
    elif 'kill torrent' in query:
        for process in (process for process in psutil.process_iter() if process.name() == "qbittorrent.exe"):
            process.kill()
            show_result('Killing Torrent, Sir')
    elif 'thanks' in query:
        show_result('Welcome. Sir')
    elif 'thank you' in query:
        show_result('Welcome. Sir')
    elif 'stop' in query:
        exit_app("Halting the Application Sir...")
    elif 'terminate' in query:
        exit_app("Terminating the Application Sir...")
    elif 'bye' in query:
        exit_app("Good Bye! Sir")
    elif 'good night' in query:
        exit_app('Good Night Darling. Have a nice dream! Bye')
    elif 'option' in query:
        show_result("Search Wikipedia ...\nOpen Youtube...\nOpen StackOverflow\nOpen Facebook\nSearch Google")
        show_result("Play Music\nPlay Video\nShow Time\nWho Are You?\nOpen Torrent\nthanks | thank you")
        show_result("Kill Music\nKill Video\nKill Chrome\nKill Torrent")
        show_result("Stop|Terminate|Bye|Good Night")
    elif 'kill music' in query:
        for process in (process for process in psutil.process_iter() if process.name() == "AIMP.exe"):
            process.kill()
            show_result('Killing AIMP, Sir')
    elif 'kill chrome' in query:
        for process in (process for process in psutil.process_iter() if process.name() == "chrome.exe"):
            process.kill()
            show_result('Killing Chrome, Sir')


if __name__ == '__main__':
    speak("Hello,Sir.")
    wishMe()

    """ task which command execute """
    
    while 1:
        query = takeCommand().lower()
        Action_Perform(query)
            





