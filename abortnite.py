import os
import time
import json

timenow =time.gmtime()
time_interval=5
total_time = 60

with open("timelog.txt") as json_file:
    timedata = json.load(json_file)
if timedata["yday"] != time.gmtime().tm_yday:
    timedata["minutes_left"] = total_time
timedata["yday"] = time.gmtime().tm_yday
json_file.close()



fortnite = os.popen("tasklist /fi \"WINDOWTITLE eq BattlEye Launcher\"").read().find("Fortnite")
unrealt = os.popen("tasklist /fi \"MEMUSAGE gt 500000\"").read().find("UE4")
steam = os.popen("tasklist /fi \"WINDOWTITLE eq Steam\"").read().find("Steam")

if fortnite == -1 or unrealt == -1 or steam == -1:
    quit()


if (timedata["minutes_left"] < 1) and (fortnite != -1 or unrealt != -1 or steam != -1):
    os.system('taskkill /f /im FortniteClient-Win64-Shipping.exe')
    os.system('taskkill /f /im UE4-Win64-Shipping.exe')
    os.system('taskkill /f /im steam.exe')
    timedata["yday"] = time.gmtime().tm_yday
    with open("timelog.txt", "w") as outfile:
        json.dump(timedata, outfile)
    quit()

timedata["minutes_left"] -= time_interval
with open("timelog.txt", "w") as outfile:
    son.dump(timedata, outfile)
