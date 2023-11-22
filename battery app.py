from tkinter import*
from tkinter import ttk
import psutil
from psutil._commomn import BatteryTime
import datetime
import time

root=Tk()
root.geometry('500x250')
root.config(bg="black")
root.overrideredirect(True)
style = ttk.Style(root)
style.layout('ProgressBarStyle',
             [('Horizontal.Progressbar.trough',
               {'children':[('Horizontal.Progressbar.pbar',
                             {'side':'right','sticky':'ns'})],
                'sticky':'nsew'}),
              ('Horizontal.Progressbar.label',{'sticky':''})])
bar = ttk.Progressbar(root, maximum=100, style='ProgressBarStyle')
bar.place(relx=0.5, rely=0.2, anchor=CENTER)
battery_life=Label(roott, font="arial 15 bold", bg='black', fg="white")
battery_life.place(relx=0.5,rely=0.5, anchor=CENTER)

def convertTime(seconds):
    get_time = time.gmtime(seconds)
    time_remain = time.strftime("%H:%M:%S", get_time)
    return time_remain

def getBatterylife():
    battery = psutil.sensors_battery()
    bar['value']= baattery.percent
    style.configure('ProgressBarStyle',text=str(battery.percent)+'%')
    battery_left = convertTime(battery.secsleft)
    if battery.secsleft == BatteryTime.POWER_TIME_UNLIMITED:
        battery_life['text']='Unplugged the battery! \n Rerun the code again'
    elif battery.secsleft == BatteryTime.POWER_TIME_UNKOWN:
        battery_life['text']='Battery life not detected \n please, run the code again!'
    else:
        battery_life['text']="Battery life :"+battery_left]
        root.after(1000, getBatterylife)
getBatteryLife()
root.mainloop()        