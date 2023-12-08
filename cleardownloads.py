import os
import shutil

def clear_downloads_folder():
    downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
    files = os.listdir(downloads_folder)
    for file in files:
        file_path = os.path.join(downloads_folder, file)
        try:
            shutil.rmtree(file_path)
        except Exception as e:
            print("Exception occured: ",e)
    print("Done clearing the downloads")

clear_downloads_folder()