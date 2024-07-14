import speech_recognition as sr
import tkinter as tk
import pyttsx3
import datetime
import webbrowser


root=tk.Tk()
root.title("Voice Assistant")


#initialising the recognizer
recognizer=sr.Recognizer()

#initialising the text to speeh engine
engine=pyttsx3.init()

#calling function to speek
def speak(text):
    engine.say(text)
    engine.runAndWait()


#calling function to listen
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio=recognizer.listen(source)


        try:
            print("Recognizing...")
            query=recognizer.recognize_google(audio)  #Recognizes the speech using google speech recognition
            print(f"You Said:{query}")
            return query.lower()
        except sr.UnknownValueError:
            print("I'am Sorry,I could not understand what you said.")
            return ""
        except sr.RequestError as e:
            print(f"Could not request results;{e}")
            return ""
# calling function to perform tasks
def perform_task(command):
    if "Hi" in command or "Hello" in command:
        speak("Hello, how can I help you today")
    elif "time" in command:
        current_time=datetime.datetime.now().strftime("%H:%M %S")
        #print(f"current time recognized:{current_time}")
        speak(f"The current time is{current_time}")
    elif "search" in command:
        speak("what do you want to explore?")
        search=listen()
        if search:
            url=f"https://www.google.com/search?q={search}"
            webbrowser.open(url)
    elif "exit" in command or "quit" in command:
        speak("Thank you")
        exit()
    else:
        speak("Apologies,I didn't understand that command,")
#calling main function
def main():
    speak("Hello, how can I help you today")
    while True:
        command=listen()
        perform_task(command)

if __name__ == "__main__":
    main()

