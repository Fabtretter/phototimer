import json
import sys
from datetime import datetime
from datetime import timedelta
from os import path

import requests

import fileutils
from config import config


# Writes in "twilight_times_path" from config.py to init 356 days of sunrise/sunset files using https://sunrise-sunset.org/api
def initSunriseSunsetFiles(lat, lng):
    print("generating config files...")
    currentDate = datetime.now()
    currentDate = currentDate.replace(day=1, month=1)
    sunsetSunriseApiCall = 'https://api.sunrise-sunset.org/json?lat=' + lat + '&lng=' + lng + '&formatted=0&date='

    callApiAndSaveFile(currentDate, sunsetSunriseApiCall)
    while not (currentDate.day == 31 and currentDate.month == 12):
        currentDate = currentDate + timedelta(days=1)
        callApiAndSaveFile(currentDate, sunsetSunriseApiCall)
        print("saved twilight file for: " + str(currentDate))
        sys.stdout.flush()

    return True


def callApiAndSaveFile(currentDate, sunsetSunriseApiCall):
    datestring = str(currentDate.year) + "-" + str(currentDate.month) + "-" + str(currentDate.day)
    filestring = str(currentDate.month) + "-" + str(currentDate.day)
    r = requests.get(sunsetSunriseApiCall + datestring)
    data = r.json()["results"]
    if data == "":
        print("no result found for: " + sunsetSunriseApiCall + datestring)
    filename = path.join(config["twilight_times_path"], filestring + ".json")
    with open(filename, 'w') as output:
        json.dump(data, output)


if (__name__ == '__main__'):
    if len(sys.argv) < 2:
        print("not enough arguments. First argument has to be latitude, second argument has to be longitude")
        print("for example: 48.26667 12.41667")
        exit()
    try:
        fileutils.try_to_mkdir(config["twilight_times_path"])

        lat = str(sys.argv[1])
        lng = str(sys.argv[2])

        initSunriseSunsetFiles(lat, lng)
    except KeyboardInterrupt:
        print("Cancelling twilight init")
