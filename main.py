import os

direction = os.getcwd()


files = os.listdir(direction)

extensions = [file.split('.')[1] for file in files if os.path.isfile(file)]
while True:
    for extension in extensions[1:]:
        if not os.path.exists(extension):
            os.mkdir(extension)
    for file in files:
        if file == 'main.py' or file == '.idea':
            continue
        os.replace(file, f"{file.split('.')[1]}/{file}")
    break
