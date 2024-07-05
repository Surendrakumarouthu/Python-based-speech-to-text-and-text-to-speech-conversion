import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pyaudio

def text_to_speech():
    text = text_entry.get("1.0", "end-1c")
    if text:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        text_entry.delete("1.0", "end")
        text_entry.insert("end", text)
    except sr.UnknownValueError:
        print("Could not understand audio")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def handle_option(option):
    if option == 1:
        text_to_speech()
    elif option == 2:
        speech_to_text()

# GUI setup
root = tk.Tk()
root.title("Speech to Text and Text to Speech")

option_label = tk.Label(root, text="Choose an option:")
option_label.pack()

option_var = tk.IntVar()
option_var.set(1)  # Default to text to speech

text_to_speech_radio = tk.Radiobutton(root, text="Text to Speech", variable=option_var, value=1)
text_to_speech_radio.pack()

speech_to_text_radio = tk.Radiobutton(root, text="Speech to Text", variable=option_var, value=2)
speech_to_text_radio.pack()

text_entry_label = tk.Label(root, text="Enter text or press the button to speak:")
text_entry_label.pack()

text_entry = tk.Text(root, height=5, width=50)
text_entry.pack()

submit_button = tk.Button(root, text="Submit", command=lambda: handle_option(option_var.get()))
submit_button.pack()

root.mainloop()
