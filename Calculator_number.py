import wolframalpha
import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wolframRamAlpha(query):
    apikey = "VQRRYV-WJ8UL76UQQL"
    requester = wolframalpha.Client(apikey)
    requested = requester.query(query)

    try:
        answer = next(requested.results).text
        return answer
    except:
        speak("the value is not answerable")

def Calc(query):
    term = str(query)
    term = term.replace("jarvis","")
    term = term.replace("multiply","*")
    term = term.replace("plus","+")
    term = term.replace("minus","-")
    term = term.replace("divide","/")

    final = str(term)
    try:
        results = wolframalpha(final)
        print(f"{results}")
        speak(results)
    except:
        speak("tthe value is not answerable")