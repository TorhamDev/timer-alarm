from time import sleep
from playsound import playsound

sleep_time = int(input("sleep time(second) : "))

sleep(sleep_time)

playsound("./alarm.wav")