import os

folders = 0
files = 0
base = os.getcwd()
for item in os.listdir(base):
    item_path = os.path.join(base, item)

    if os.path.isdir(item_path):
        folders += 1
    elif os.path.isfile(item_path):
        files += 1

print(f"folders: {folders}, files: {files}")