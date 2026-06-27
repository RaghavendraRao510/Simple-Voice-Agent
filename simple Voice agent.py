import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    print(f"Agent: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        # Reduce background noise impact
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-US')
        print(f"You said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that. Could you repeat?")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def run_agent():
    speak("Hello! I am online. How can I help you?")
    
    while True:
        command = listen_command()
        
        if not command:
            continue
            
        if "hello" in command:
            speak("Hi there! Hope you are having a great day.")
            
        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}")
            
        elif "open google" in command:
            speak("Opening Google.")
            webbrowser.open("https://www.google.com")
            
        elif "stop" in command or "exit" in command or "bye" in command:
            speak("Goodbye!")
            break
        else:
            speak("I heard you, but I don't know that command yet.")

if __name__ == "__main__":
    run_agent()