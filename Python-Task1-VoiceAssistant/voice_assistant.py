import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You:", command)
        return command.lower()

    except sr.UnknownValueError:
        speak("Sorry, I didn't understand. Please repeat.")
        return ""

    except sr.RequestError:
        speak("Speech service is unavailable right now.")
        return ""


def main():
    speak("Hello! I am your voice assistant. How can I help you?")

    while True:
        command = listen()

        if not command:
            continue

        if "hello" in command or "hi" in command:
            speak("Hello! Nice to talk to you.")

        elif "time" in command:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            speak(f"The current time is {current_time}.")

        elif "date" in command:
            current_date = datetime.datetime.now().strftime("%d %B %Y")
            speak(f"Today's date is {current_date}.")

        elif "search" in command:
            query = command.replace("search", "", 1).strip()

            if query:
                speak(f"Searching for {query}")
                url = "https://www.google.com/search?q=" + query.replace(" ", "+")
                webbrowser.open(url)
            else:
                speak("Please tell me what you want to search.")

        elif "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break

        else:
            speak("I didn't understand that command. Please repeat.")


if __name__ == "__main__":
    main()
