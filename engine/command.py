import pyttsx3


def speak(text):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 164)
    print(voices)
    engine.say(text)
    engine.runAndWait()

speak("India is my country, all indians are my brothers and sisters")