import pyttsx3;
import datetime;
import speech_recognition as sr;
import wikipedia;
import webbrowser;
import os;

engine = pyttsx3.init('sapi5');
voices = engine.getProperty('voices');
print(voices[1].id);
engine.setProperty('voice', voices[1].id);

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishUser():
    hour = int(datetime.datetime.now().hour);
    print(hour)
    if hour >=0 and hour < 12:
        speak('Hello Ramkrishna, Good Morning!')
    elif hour >= 12 and hour < 18:
        speak('Hello Ramkrishna, Good Afternoon!')
    else:
        speak('Hello Ramkrishna, Good Enening!') 

    speak("How can i help you?")    

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...");
        r.energy_threshold = 300
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizer...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Sorry, I did not get you, could you please repeat")
        speak("Sorry, I did not get you, could you please repeat")
        return "None"
    return query    


if __name__ == "__main__":
    wishUser()
    while True:
          query = takeCommand().lower()
          
          if 'wikipedia' in query:
              speak("Please wait, Searching wikipedia")
              query = query.replace("wikipedia", "")
              results = wikipedia.summary(query, sentences=2)
              speak("According to wikipedia")
              speak(results)

          elif 'open youtube' in query:
                webbrowser.register('google-chrome', None)
                webbrowser.open("https://www.youtube.com/")

          elif 'play music' in query:
                music_dir = 'C:\\Users\\Lenovo\\Music\\mymusic'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

          elif 'the time' in query:
                strTime = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"Sir, the time is {strTime}")

          elif 'open sts' in query:
                sts_path = "F:\\All Software's\\Programming Softwares\\IDE\\sts-4.5.0.RELEASE\\SpringToolSuite4.exe"
                os.startfile(sts_path)   

          elif 'open notepad' in query:
                sts_path = "C:\\Program Files (x86)\\Notepad++\\notepad++.exe"
                os.startfile(sts_path)   
   
          elif 'open facebook' in query:
                webbrowser.open("https://www.facebook.com/ram.sitap.1/")



