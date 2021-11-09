import os
import datetime
from playsound import playsound

os. system('clear')

alarmH = int(input("Please specify HOUR (1-12)")) ## input for hour ##
alarmM = int(input("Please specify MINUTES (0-59)")) ## input for minute ##
amPm = str(input("am or pm? ")) ## input for am or pm ##

os. system('clear')

print("Waiting for alarm",alarmH,alarmM,amPm)

if (amPm == "pm"):
        alarmH = alarmH + 12 ## simple if statement which adds 12 hours to the input time when specifying PM ##
while(1 == 1):
    if(alarmH == datetime.datetime.now().hour and
        alarmM == datetime.datetime.now().minute) : ## If set time matches with current time, then print message and play sound ##
        print("Time to wake up")
        playsound('D:\Docs\HL2_SFX.mp3') ## destination to sound file ##
        break