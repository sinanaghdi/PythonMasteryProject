# imports and global variables
import tkinter as tk
from datetime import datetime
from tkinter import messagebox

Window = tk.Tk()
alarm_time = None
Window.title("Alarm Clock App")
Window.resizable(width=False,height=False)
Window.geometry("400x300")
# function for getting current time
def get_current_time():
    current_time = datetime.now()
    time_label.configure(text=current_time.strftime("%H:%M:%S"))
    compare_alarm_with_current_time(current_time)
    Window.after(1000,get_current_time)


# function set alarm
def set_alarm():
    global alarm_time
    current_time = datetime.now()
    alarm_time = current_time.replace(hour = int(hour_alarm_entry.get()),
        minute = int(minute_alarm_entry.get()),second=0,microsecond=0)
    latest_alarm_button.configure(text=alarm_time.strftime("%H:%M:%S"))
     



# function for comparing time with alarm
def compare_alarm_with_current_time(current_time):
    global alarm_time
    if alarm_time is not None and current_time>=alarm_time:
        messagebox.showinfo('showinfo','your alarm happened!')
        latest_alarm_button.configure(text="No alarm has been set")
        alarm_time = None




# ui design

# text time 
time_label = tk.Label(Window, text='12:30:30',font=("Tahoma",32))
time_label.pack()




# text time hour
# input Entry
tk.Label(Window, text='Hour').pack()
hour_alarm_entry = tk.Entry(Window)
hour_alarm_entry.pack()


# text input minute
#input Entry
tk.Label(Window, text='Minute').pack()
minute_alarm_entry = tk.Entry(Window)
minute_alarm_entry.pack()



#button set alarm
tk.Button(Window,text="Set Alarm",command=set_alarm).pack()

# showing last alarm
latest_alarm_button = tk.Label(Window,text='No Alarm Has Been Set!')
latest_alarm_button.pack()
# running application
get_current_time()
Window.mainloop()
