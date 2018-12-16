import os

from config import config


def try_to_mkdir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def prepare_dir_in_date_format(base, datetime):
    path = os.path.join(base, str(datetime.year), str(datetime.month), str(datetime.day))
    try_to_mkdir(path)

    return path


def getConfigFileName(date):
    filestring = str(date.month) + "-" + str(date.day)
    return os.path.join(config["twilight_times_path"], filestring + ".json")