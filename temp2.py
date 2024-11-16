import tkinter as tk
from tkinter import *
from tkinter.ttk import Combobox
import pyttsx3
import os

# Set up main window
root = Tk()
root.title("Text to Audio")
root.geometry("576x1024")  # Adjusted for 16:9 vertical layout
root.resizable(False, False)
root.configure(bg="#A9A9A9")  # Background color

engine = pyttsx3.init()

def speaknow():
    text = text_area.get(1.0, END).strip()
    if not text:
        return  # Do nothing if the text area is empty

    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    # Set voice based on gender
    if gender == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    # Set speech speed
    if speed == "Fast":
        engine.setProperty('rate', 250)
    elif speed == "Normal":
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    engine.say(text)
    engine.runAndWait()

def download():
    text = text_area.get(1.0, END).strip()
    if not text:
        return  # Do nothing if the text area is empty

    gender = gender_combobox.get()
    speed = speed_combobox.get()
    voices = engine.getProperty('voices')

    if gender == 'Male':
        engine.setProperty('voice', voices[0].id)
    else:
        engine.setProperty('voice', voices[1].id)

    if speed == "Fast":
        engine.setProperty('rate', 250)
    elif speed == "Normal":
        engine.setProperty('rate', 150)
    else:
        engine.setProperty('rate', 60)

    # Save audio to file
    engine.save_to_file(text, 'output_audio.mp3')
    engine.runAndWait()
    print("Audio saved as 'output_audio.mp3'")

# App logo and icons
image_icon = PhotoImage(file="Dot_logo.png.png")
root.iconphoto(False, image_icon)

# Top frame
Top_frame = Frame(root, bg="white", width=576, height=100)
Top_frame.place(x=0, y=0)

Logo = PhotoImage(file="logo1.png")
Label(Top_frame, image=Logo, bg="white").place(x=10, y=5)

Label(Top_frame, text="𝐓𝐄𝐗𝐓 𝐓𝐎 𝐀𝐔𝐃𝐈𝐎", font="arial 20 bold", bg="white", fg="black").place(x=120, y=30)

# Text area
text_area = Text(root, font="Robot 15", bg="white", relief=GROOVE, wrap=WORD)
text_area.place(x=10, y=150, width=550, height=300)

# Labels for voice and speed
Label(root, text="VOICE", font="arial 15 bold", bg="#000000", fg="white").place(x=100, y=480)
Label(root, text="SPEED", font="arial 15 bold", bg="#000000", fg="white").place(x=350, y=480)

# Gender combobox
gender_combobox = Combobox(root, values=['Male', 'Female'], font="arial 14", state='r', width=10)
gender_combobox.place(x=70, y=520)
gender_combobox.set('Male')

# Speed combobox
speed_combobox = Combobox(root, values=['Fast', 'Normal', 'Slow'], font="arial 14", state='r', width=10)
speed_combobox.place(x=320, y=520)
speed_combobox.set('Normal')

# Speak button
imageicon = PhotoImage(file="R (4).png")
btn = Button(root, text="Speak", compound=LEFT, image=imageicon, width=150, font="arial 14 bold", command=speaknow)
btn.place(x=100, y=600)

# Save button
imageicon2 = PhotoImage(file="download.png")
save = Button(root, text="Save", compound=LEFT, image=imageicon2, width=150, bg="#39c790", font="arial 14 bold", command=download)
save.place(x=320, y=600)

root.mainloop()
