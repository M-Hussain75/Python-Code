import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime

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
    else:
        speak("I'm not sure how to help with that.")

# Main function to run the assistant
def main():
    speak("Hello, I am Jarvis. How can I assist you?")
    while True:
        command = take_command()
        if command:
            if 'stop' in command:
                speak("Goodbye!")
                break
            else:
                execute_command(command)
        else:
            speak("I didn't catch that. Please try again.")

if __name__ == "__main__":
    main()
