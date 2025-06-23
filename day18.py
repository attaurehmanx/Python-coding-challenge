# Week 3: Functions, Modules & File Handling
# ------------------------------------------
# Day 18 – Basic Alarm Clock: Use datetime and time modules.

import datetime
import os
import platform
import time

def clock():
    # user alarm time 
    user_alarm = input("Enter alarm time in HH:MM:SS (24-Hour-format)")
    # separating time in HH:MM:SS  
    alarm_hour, alarm_min, alarm_sec = map(int, user_alarm.split(":"))

    while True:
        # real time 
        now = datetime.datetime.now()

        curr_time = now.strftime('%H:%M:%S')
        # curr_time equal to user_alarm print the msg 
        if curr_time == user_alarm:
            print("Time to wake-up")
        # if system is window it trigger alarm if the device is other then execute the else 
            if platform.system() == "Windows":
                for _ in range(5):
                    os.system("echo \a")
                    print("hi")
                    # pause the time for 1 sec 
                    time.sleep(1)
            else:
                for _ in range(5):
                    print('\n')
                    print("hi")
                    time.sleep(1)
                break
            time.sleep(1)

if __name__ == '__main__':
    clock()