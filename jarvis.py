#new code
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os
import random
import requests

# Initialize the recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak a given text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to take a command from the user
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            print("Recognizing...")
            command = recognizer.recognize_google(audio)
            print(f"Recognized command: {command}")
            return command.lower()
    except sr.UnknownValueError:
        print("Speech recognition could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Function to execute tasks based on command
def execute_command(command):
    if 'open youtube' in command:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
    elif 'time' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {time}")
    elif 'open google' in command:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")
    elif 'open facebook' in command:
        speak("Opening Facebook")
        webbrowser.open("https://www.facebook.com")
    elif 'play music' in command:
        speak("Playing music")
        os.system("start wmplayer")  # Adjust to your preferred music player
    elif 'tell me a joke' in command:
        jokes = [
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised.",
            "What’s orange and sounds like a parrot? A carrot!"
        ]
        joke = random.choice(jokes)
        speak(joke)
    elif 'weather' in command:
        speak("Fetching the weather for you.")
        # You can use an API like OpenWeatherMap to get the weather data.
        # For simplicity, let's pretend we're fetching it.
        weather = "It's sunny with a high of 25°C."
        speak(weather)
    elif 'open twitter' in command:
        speak("Opening Twitter")
        webbrowser.open("https://www.twitter.com")
    elif 'search' in command:
        search_query = command.split('search', 1)[1]
        speak(f"Searching for {search_query}")
        webbrowser.open(f"https://www.google.com/search?q={search_query}")
    elif 'stop' in command:
        speak("Goodbye!")
        return True
    else:
        speak("I'm not sure how to help with that.")
    return False

# Main function to run the assistant
def main():
    speak("Hello, I am Jarvis. How can I assist you?")
    while True:
        command = take_command()
        if command:
            stop = execute_command(command)
            if stop:
                break
        else:
            speak("I didn't catch that. Please try again.")

if __name__ == "__main__":
    main()
