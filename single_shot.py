import logging
import os
import sys
import time
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
    exposureCalc1 = exposureCalc()

    take_shot = False
    mode = config["mode"]
    logging.info("Mode: " + mode)

    if mode == "always":
        take_shot = True
    if mode == "config":
        take_shot = exposureCalc1.take_shot(config["am"], config["pm"], int(time.strftime("%H%M")))
    if mode == "twilight":
        take_shot = exposureCalc1.isBetweenSunriseAndSunset(datetime.utcnow())

    if (take_shot):
        now = datetime.now()
        path = fileutils.prepare_dir_in_date_format(config["base_path"], now)

        name = generate_file_name(now);
        logging.info("Taking shot: " + name)
        file_name = os.path.join(path, name)

        os_command = make_os_command(config, "auto", file_name)
        os.system(os_command)
        logging.info("Written: " + file_name)
    else:
        logging.info("No picture was shot because its dark outside")


def generate_file_name(now):
    return str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(now.minute) + str(now.second) + ".jpg"


if (__name__ == '__main__'):
    logging.basicConfig(filename='single_shot.log', level=logging.DEBUG)
    if len(sys.argv) < 1:
        exit()
    else:
        try:
            shoot_picture()
        except KeyboardInterrupt:
            logging.info("Cancelling take.py")
