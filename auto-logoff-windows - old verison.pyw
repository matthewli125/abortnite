import os
import time
import json

timenow =time.gmtime()

with open("timelog.txt") as json_file:
    timedata = json.load(json_file)
if timedata["yday"] != time.gmtime().tm_yday:
    timedata["minutes_left"] = 60
timedata["yday"] = time.gmtime().tm_yday
json_file.close()

while True:
    while True:
        time.sleep(15)
        fortnite = os.popen("tasklist /fi \"WINDOWTITLE eq BattlEye Launcher\"").read().find("Fortnite")
        unrealt = os.popen("tasklist /fi \"MEMUSAGE gt 500000\"").read().find("UE4")
        steam = os.popen("tasklist /fi \"WINDOWTITLE eq Steam\"").read().find("Steam")
        #print("not open")
        if fortnite != -1 or unrealt != -1 or steam != -1:
            break;
        
    timedata["yday"] = time.gmtime().tm_yday
    with open("timelog.txt", "w") as outfile:
        json.dump(timedata, outfile)


    for i in range(timedata["minutes_left"]):
        time.sleep(60)
        #print("open")
        timedata["minutes_left"]-=1
        #print("time left = {} minutes".format(timedata["minutes_left"]))
        with open("timelog.txt", "w") as outfile:
            json.dump(timedata, outfile)
        fortnite = os.popen("tasklist /fi \"WINDOWTITLE eq BattlEye Launcher\"").read().find("Fortnite")
        unrealt = os.popen("tasklist /fi \"PID eq 3320\"").read().find("UE4")
        steam = os.popen("tasklist /fi \"WINDOWTITLE eq Steam\"").read().find("Steam")
        if fortnite == -1 or unrealt == -1 or steam == -1:
            break;


    while True:
        fortnite = os.popen("tasklist /fi \"WINDOWTITLE eq BattlEye Launcher\"").read().find("Fortnite")
        unrealt = os.popen("tasklist /fi \"PID eq 3320\"").read().find("UE4")
        steam = os.popen("tasklist /fi \"WINDOWTITLE eq Steam\"").read().find("Steam")
        time.sleep(1)
        #print("kill")
        if (timedata["minutes_left"] < 1) and (fortnite != -1 or unrealt != -1 or steam != -1):
            os.system('taskkill /f /im FortniteClient-Win64-Shipping.exe')
            os.system('taskkill /f /im UE4-Win64-Shipping.exe')
            os.system('taskkill /f /im steam.exe')
            timedata["yday"] = time.gmtime().tm_yday
            with open("timelog.txt", "w") as outfile:
                json.dump(timedata, outfile)
        else:
            break



