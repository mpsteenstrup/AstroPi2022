import os

import pathlib

path = pathlib.Path(__file__).parent.absolute()

for i in os.listdir(path):
    name = i.split(' ')
    if ' ' in i:
        os.rename(i, name[0] + ".py")
#print(os.listdir(path))
