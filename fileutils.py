import os

def try_to_mkdir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)

def prepare_dir_in_date_format(base, datetime):
    path = os.path.join(base, str(datetime.year), str(datetime.month), str(datetime.day))
    try_to_mkdir(path)

    return path