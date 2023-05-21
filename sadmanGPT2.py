import openai
import pyttsx3
import speech_recognition as sr

openai.api_key="your_api"

engine= pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def audioTotext():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        r.pause_threshold=2
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language="en-IN")#converting audio to text
        return query
    except Exception as e:
        print(e)
        speak("Please speack once more...")
        audioTotext()

def askUltron(question):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=question,
        temperature=0.3,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.5,
        presence_penalty=0.6,
    )
    data= response.choices[0].text
    return data.strip()

# speak("Hi!Everyone. What's up?")
# while True:
#     query=input("Ask a question from Ultron: ")
#     outputText=askUltron(query)
#     print(outputText)
while True:
    inputText=audioTotext()
    print(inputText)
    outputText=askUltron(inputText)
    print("\nSadman: "+ outputText)
    speak(outputText)
