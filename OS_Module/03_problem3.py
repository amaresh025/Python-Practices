import os

base = os.getcwd()


for folder in os.listdir(base):
    path = os.path.join(base, folder)
    try:
        if os.path.isdir(path):
            if not os.listdir(path):
                print(f"empty_folders: {folder}")

                os.rmdir(path)
    except OSError:
        pass