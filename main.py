"""
by: mohamed fares
Implements an alarm clock functionality using the Tkinter GUI library.

The `alarm_clock` function takes the hour, minute, and second values as input and continuously checks the current time against the alarm time. When the current time matches the alarm time, it plays a sound using the `winsound` module.

The GUI interface allows the user to set the alarm time by selecting the hour, minute, and second values from dropdown menus. When the "Submit" button is clicked, the `alarm_clock` function is called with the selected values.
"""
# Import all the necessary modules

from tkinter import *
import winsound

import datetime

import time


def alarm_clock(hr, min, sec):
  while True:
     alarm_time = f"{hr}: {min}: {sec}"

     # Getting current time by using .striftime() method of the datetime module's datetime file's now function
     current_time = datetime.datetime.now().strftime("%H:%M:%S")

     if current_time == alarm_time:
        time.sleep(1)
        print("Time to wake up, buddy!")
        # Playing a sound when the current time is the same as the alarm time
        # The .wav file should be in the same directory as the python code
        winsound.PlaySound('anyfile.wav', winsound.SND_ASYNC)









# Setting the main screen
root = Tk()
root.title("Project(mohamedfarez)Alarm Clock")
root.geometry("270x300")
root.resizable(False, False)

# Creating and placing all the components of the window
Label(root, text='When do you want to wake up?\n(Enter in 24-hour format)', font=("Comic Sans MS", 13), wraplength=root.winfo_width()).place(x=0, y=0)

Label(root, text='Hour', font=("Book Antiqua", 11), wraplength=root.winfo_width()).place(x=50, y=70)
Label(root, text='Minute', font=("Book Antiqua", 11), wraplength=root.winfo_width()).place(x=100, y=70)
Label(root, text='Second', font=("Book Antiqua", 11), wraplength=root.winfo_width()).place(x=160, y=70)

hours = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
minutes = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']
seconds = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09']

for i in range(10, 24):
  hours.append(i)

for i in range(10, 61):
  minutes.append(i)
  seconds.append(i)

hour = StringVar(root)
hour.set(hours[0])
OptionMenu(root, hour, *hours).place(x=40, y=100)

minute = StringVar(root)
minute.set(minutes[0])
OptionMenu(root, minute, *minutes).place(x=100, y=100)

second = StringVar(root)
second.set(seconds[0])
OptionMenu(root, second, *seconds).place(x=160, y=100)

submit_btn = Button(root, text='Submit', bg='CadetBlue4', command=lambda: alarm_clock(hour.get()[:2], minute.get()[:2], second.get()[:2]))
submit_btn.place(x=100, y=150)



