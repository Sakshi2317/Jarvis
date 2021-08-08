import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')  #API to get voice 
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: 
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    
    else:
        speak("Good Evening!")

    speak("I am Jarvis ma'am, Please tell me how may I help you?")


def takeCommand():
    # It takes microphone input from user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...") 
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    chorme_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    while True:
        query = takeCommand().lower()
        # logic for ecxecuting tasks based on query
        if 'wikipedia' in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results )
        
        elif 'open youtube' in query:
            webbrowser.get(chorme_path).open("youtube.com")

        elif 'open google' in query:
            webbrowser.get(chorme_path).open("google.com")

        elif 'open linkedin' in query:
            webbrowser.get(chorme_path).open("linkedin.com")

        elif 'show memories' in query:
            memory_dir = 'C:\\Users\\lenovo\\Pictures\\Sakshi 1'
            pics = os.listdir(memory_dir)
            os.startfile(os.path.join(memory_dir))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Ma'am, The time is {strTime}")