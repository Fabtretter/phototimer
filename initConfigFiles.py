import pickle
import sys
from datetime import datetime
from datetime import timedelta
from os import path

import requests

import fileutils
from config import config


# Writes in "twilight_times_path" from config.py to init 356 days of sunrise/sunset files using https://sunrise-sunset.org/api
def initSunriseSunsetFiles():
    currentDate = datetime.now()
    currentDate = currentDate.replace(day=1, month=1)
    sunsetSunriseApiCall = 'https://api.sunrise-sunset.org/json?lat=48.26667&lng=12.41667&formatted=0&date='

    callApiAndSaveFile(currentDate, sunsetSunriseApiCall)
    while not (currentDate.day == 31 and currentDate.month == 12):
        currentDate = currentDate + timedelta(days=1)
        callApiAndSaveFile(currentDate, sunsetSunriseApiCall)
        print("saved twilight file for: " + str(currentDate))
        sys.stdout.flush()

    return True


def callApiAndSaveFile(currentDate, sunsetSunriseApiCall):
    datestring = str(currentDate.month) + "-" + str(currentDate.day)
    r = requests.get(sunsetSunriseApiCall + datestring)
    data = r.json()
    filename = path.join(config["twilight_times_path"], datestring + ".p")
    with open(filename, 'wb') as output:
        pickle.dump(data, output, pickle.HIGHEST_PROTOCOL)


if (__name__ == '__main__'):
    try:
        fileutils.try_to_mkdir(config["twilight_times_path"])
        initSunriseSunsetFiles()
    except KeyboardInterrupt:
        print("Cancelling twilight init")
