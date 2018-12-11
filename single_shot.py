import os
import sys
from datetime import datetime

import fileutils
from camera import exposureCalc
from config import config


def make_os_command(config, exposureMode, file_name):
    height = config["height"]
    width = config["width"]

    os_command = "/opt/vc/bin/raspistill -q " + str(config["quality"]) + " "
    if (config["flip_horizontal"]):
        os_command = os_command + "-hf "
    if (config["flip_vertical"]):
        os_command = os_command + "-vf "

    os_command = os_command + "-h " + str(height) + \
                 " -w " + str(width) + \
                 " --exposure " + exposureMode + \
                 " --metering " + config["metering_mode"] + \
                 " -o " + file_name
    return os_command


def shoot_picture():
    take_shot = exposureCalc.isBetweenSunriseAndSunset(datetime.now())

    if (take_shot):
        now = datetime.now()
        path = fileutils.prepare_dir_in_date_format(config["base_path"], now)

        name = generate_file_name(now);
        print("Taking shot: " + name)
        file_name = os.path.join(path, name)

        os_command = make_os_command(config, "auto", file_name)
        os.system(os_command)
        print("Written: " + file_name)
    else:
        print("Shot cancelled during hours of darkness")


def generate_file_name(now):
    return str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".jpg"


if (__name__ == '__main__'):
    if len(sys.argv) < 1:
        exit()
    else:
        try:
            basePath = config["base_path"]
            shoot_picture()
        except KeyboardInterrupt:
            print("Cancelling take.py")
