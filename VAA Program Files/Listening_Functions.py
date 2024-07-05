import speech_recognition
from googletrans import Translator
from vosk import Model, KaldiRecognizer
import pyaudio

def Listen_English(): 
    command = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("")
        print("Listening...")
        print("")
        command.pause_threshold = 1
        command.energy_threshold = 300
        audio = command.listen(source)
    try:
        print("Recognizing...")   
        print("")
        query = command.recognize_google(audio, language='en-in')
        print("")
        print(f"Your Command-:  {query}\n")
        print("")
    except Exception as e:
        print(e)   
        print("Sir, say it again please...")
        print("")
        return "None"
    query = str(query)    
    return query.lower()

def Listen_Hindi(): 
    command = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("")
        print("Listening...")
        print("")
        command.pause_threshold = 1
        command.energy_threshold = 300
        audio = command.listen(source)
    try:
        print("Recognizing...")
        print("")
        query = command.recognize_google(audio, language='hi')
        print("")
        print(f"Your Command-:  {query}\n")
        print("")
    except Exception as e:
        print(e)   
        print("Sir, say it again please...")
        print("")
        return "None"
    query = str(query)    
    return query.lower()

def Language_Translation(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line, "en-in")
    data = result.text
    print(f"Your Command-: {data}")
    print("")
    return data

def Microphone_Connection():
    query = Listen_Hindi()
    Translated_query = Language_Translation(query)
    return Translated_query

model = Model("C:\\Users\\anike\\OneDrive\\Desktop\\Python\\Virtual-AI-Assistant\\vosk-model")
recognizer = KaldiRecognizer(model, 16000)
mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

def Listen_Offline():
    print("")
    print("Listening...")
    print("")
    while True:
        data = stream.read(4096)
        if recognizer.AcceptWaveform(data):
            text = recognizer.Result()
            RefinedText = text[14:-3]
            print(f"Your Command-: {RefinedText}")
            print("")
            if len(RefinedText)>0:
                return RefinedText
            else:
                break
