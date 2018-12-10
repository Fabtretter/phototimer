import os

def try_to_mkdir(path):
    if os.path.exists(path) == False:
        os.makedirs(path)