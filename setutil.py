import json
import time
import os

timenow =time.gmtime()
total_time = 60 #set this time to how many minutes you want
scriptpath = "abortnite.pyw" #set this path to wherever you put your script
frequency = 5

timedata = {}
timedata['start_time_raw'] = int(time.time())
timedata['start_time'] = (timenow.tm_hour, timenow.tm_min)
timedata["yday"] = timenow.tm_yday
timedata['minutes_left'] = total_time

with open("timelog.txt", "w") as outfile:
    json.dump(timedata, outfile)


os.system("schtasks /create /sc minute /mo {} /tn \"abortnite\" /tr {}".format(frequency, scriptpath))
