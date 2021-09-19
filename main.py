import os

direction = os.getcwd()


files = os.listdir(direction)
extensions = [file.split('.')[1] for file in files if os.path.isfile(file)]

while True:
    for extension in extensions:
        if not os.path.exists(extension):
            os.mkdir(extension)
    for file in files:
        if file == 'main.py' or len(file.split('.')[0]) == 0:
            continue
        os.replace(file, f"{file.split('.')[1]}/{file}")
    break

