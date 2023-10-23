import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os


engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")

    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening") 
    speak("your brother here ")
    speak("how may i help you")
def takeCommand():

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=1   
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print("user said:",query)
    except Exception as e:
        print("say that again please...")
        return "NONE"
    return query
           
if __name__=="__main__":
    speak("hi")
    wishMe()
    while True:    
        query=takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query=query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences=3)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif  'open youtube' in query:
            webbrowser.open("youtube.com")  

        elif  'open google' in query:
            webbrowser.open("google.com") 
        elif  'open cuims' in query:
            webbrowser.open("cuims.com")
        elif  'open cuims' in query:
            webbrowser.open("cuims.com")        
        #elif  'play music on youtube ' in query:
           # webbrowser.open("music youtube.com")
        elif  'the time ' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strTime}")
        elif 'open code' in query:
            codePlace="C:\\Users\\rajsu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePlace)