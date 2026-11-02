'''
JERVIS - Voice Assistant using raw Python

Modules used:
1. SpeechRecognition: Captures audio and converting it into written text
2. Pyttsx3: Converts text into spoken audio (Text-to-Speech)
3. wikipedia: Searches and retrieves information from Wikipedia
4. pyjokes: Generates programming jokes
5. datetime: Fetches the current date and time
6. webbrowser: Opens websites in the default web browser
'''

# TODO 1: Import all necessary modules

import speech_recognition as sr
import pyttsx3 
import wikipedia
import pyjokes
import datetime
import webbrowser


# TODO: 2. Initialize the Speech Engine and Recognizer

# Initialize the text-to-speech engine. Use this engine whenever Jervis needs to speek.
engine = pyttsx3.init()

# Initialize the speech recognizer which help us convert our voice into written text.
recognizer = sr.Recognizer()


# TODO: 3. Text-to-Speech Implementation

def speaker(text):
    # Display Jervis's response in the terminal.
    print('Jervis:', text)

    try:
        # Convert the given text into spoken audio.
        engine.say(text)
        # Wait until Jervis finishes speaking.
        engine.runAndWait() 
    
    except Exception as e:
        print(f'Speech Error: {e}')


# TODO: 4. Speech-to-Text Implementation

def take_user_command():
    # Open the microphone to capture user's voice.
    with sr.Microphone() as source:
        print('Listenning...')

        # Record the user's voice.
        audio = recognizer.listen(source)

        try:
            # Convert the recorded audio into written text.
            # Here, we uses Google's speech recognition service
            user_command = recognizer.recognize_google(audio)

            # Display the speech-to-text understood by the assistant
            print(f'You: {user_command}')

            # Convert the text into lowercase and return it.
            return user_command.lower()

        except sr.UnknownValueError:
            # Occurs when the assistant cannot understand the voice.
            speaker("Sorry! I couldn't understand your speech")
            return ""
        
        except sr.RequestError:
            # Occurs when the speech recognition service is unavailable
            speaker("Please check your internet connection.")
            return ""
        

# TODO: 5. Greet user

def greet():
    # Get the current time in hour (0 - 23)
    hour = int(datetime.datetime.now().hour)

    # Check the current time and greet the user.
    if hour <= 12:
        speaker('Good Morning!')
    elif hour <= 17:
        speaker('Good Afternoon!')
    else:
        speaker('Good Evening!')

    # Introduce the voice assistant
    speaker("Hey, I'm Jervis. Your 24/7 voice assistant. How can I help you?")


# TODO: 6. Jervis Voice Assistant implementation

def jervis_voice_assistant():
    # At first the voice assistant greets the user
    greet()

    # Keep the assistant running until the user says goodbye.
    while True:
        # Take the user input using the microphone.
        user_input = take_user_command()

        # If no voice is recognized, listen again
        if user_input == "":
            continue


        # Current time command
        if "time" in user_input or "current time" in user_input or "today's time" in user_input:
            # Get the current time in hours, minutes, and seconds.
            time = datetime.datetime.now().strftime("%H:%M:%S")

            # Speak the current time.
            speaker(f"Today's current time is {time}.")


        # Open google command
        elif "google" in user_input or "open google" in user_input:
            # Speak the text
            speaker("Opening Google...")

            # Open Google in the default web browser
            webbrowser.open("https://www.google.com")


        # Open youtube command
        elif "youtube" in user_input or "open youtube" in user_input:
            # Speak the text
            speaker("Opening YouTube...")

            # Open YouTube in the default web browser
            webbrowser.open("https://www.youtube.com")


        # Open or ask chatgpt command
        elif "chatgpt" in user_input or "open chatgpt" in user_input or "ask chatgpt" in user_input:
            # Speak the text
            speaker("Opening ChatGPT...")

            # Open ChatGPT in the default web browser
            webbrowser.open("https://www.chatgpt.com")


        # Joke command
        elif "joke" in user_input or "say a joke" in user_input or "tell a joke" in user_input:
            # Generate a random programming joke
            speaker(pyjokes.get_joke())


        # Wikipedia search command
        elif "wikipedia" in user_input or "search wikipedia" in user_input:
            # Speak the text
            speaker("Searching on Wikipedia...")

            # Remove command-related words/phrases from the user's sentence
            search_query = user_input.replace('search wikipedia for', '').strip()

            try:
                # Search wikipedia and retrieve the first 5 sentences
                result = wikipedia.summary(user_input, sentences=5)

                # Speak the search result
                speaker(f"According to Wikipedia: {result}")

            except:
                # Handle errors if the search fails.
                speaker("Sorry! I couldn't find anything.")
        
        elif "exit" in user_input or "close" in user_input or "bye" in user_input:
            # Speak the paragraph.
            speaker("""
            Thanks for using Jervis voice assistant.
            See you next time. 
            Jervis Voice Assistant 2026.
            """)
            # Stop the loop and terminate the assistant.
            break

        else:
            # If none of the conditions match, speak the text.
            speaker("I didn't understand your command. Please try again.")


# TODO: 5. Run the Jervis voice assistant
if __name__ == "__main__":
    jervis_voice_assistant()