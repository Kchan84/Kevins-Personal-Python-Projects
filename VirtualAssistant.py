import speech_recognition #speech to text
import pyttsx3 #text to speech
import pywhatkit
import wikipedia
import datetime

#When called the VA will talk.
def VAhelp(text):
    
    if ('play' in text):
        song = text.replace("play", "")
        VA.say(f"Now playing {song}")
        pywhatkit.playonyt(song)
        VA.runAndWait()

    elif("who is" in text):
        search = text.replace("who is", "")
        info = wikipedia.summary(search, 1)
        VA.say(f"{info}")
        VA.runAndWait()

    elif("where is" in text):
        search = text.replace("where is", "")
        info = wikipedia.summary(search, 1)
        VA.say(f"{info}")
        VA.runAndWait()

    elif("what is" in text):
        search = text.replace("what is", "")
        info = wikipedia.summary(search, 1)
        VA.say(f"{info}")
        VA.runAndWait()

    elif("time" in text):
        time = datetime.datetime.now().strftime('%I:%M %p')
        VA.say(f"The current time is {time}")
        VA.runAndWait()
    
def userVoiceInput():
    while True:

        try:

            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio)
                text = text.lower()

                if (VAname in text):
                    text = text.replace(f"{VAname}", "")
                    VAhelp(text)
                
                print(f'{name}: {text}')
        except:
            recognizer = speech_recognition.Recognizer()
            continue


#Declaring Objects - Speech Recognizer and text to speech engine
recognizer = speech_recognition.Recognizer()
VA = pyttsx3.init()

#changing virtual assitant's voice
voices = VA.getProperty('voices')
VA.setProperty('voice', voices[1].id)

#Initial greeting to user
name = input("What is your name?")
VAname= input("What would you like your virtual assitant's name to be?")

VA.say(f"Hello {name}, I am {VAname}, your virtual assistant! What can I help you with? ")
VA.runAndWait()
userVoiceInput()
