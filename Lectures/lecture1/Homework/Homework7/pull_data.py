from read_data import *
from keys import keys

def pull_line(key, value, path="data.txt"):
    data = input_read(path)
    try:
        return [line for line in data if line[key] == value]
    except:
        return ['No key']
