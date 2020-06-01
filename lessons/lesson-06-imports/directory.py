import os

directory = os.getcwd()

for entry in os.scandir(directory):
    if(entry.is_file()):
        print(entry.name)

