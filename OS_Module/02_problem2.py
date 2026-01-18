import os 

base = os.getcwd()
folders = ["data", "log", "report"]

for folder in folders:
    path = os.path.join(base, folder)

    if not os.path.exists(path):
        os.mkdir(path)

print(os.listdir(base))