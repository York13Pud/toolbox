# --- Import the required libraries:
from pathlib import Path
from PIL import Image

import json
import logging
import os


# --- Define constants and variables:
APP_DIR = Path(__file__).resolve().parent
EXPORT_DIR_NAME = "icons"
EXPORT_DIR_PATH = Path(APP_DIR, EXPORT_DIR_NAME)


file_name = "app-icon"
file_extensions = ["jpg", "jpeg", "png"]
file_found = False


image_file_sizes_list = "image-sizes.json"
testing = ""
testing_list_length = len(file_extensions)
testing_loop_count = 1


# --- Check for the presence of the app-icon image:
for extension in file_extensions:
    if testing == "":
        try:
            testing = Image.open(f"{APP_DIR}/test.{extension}")
        except FileNotFoundError:
            print(f"File testing.{extension} not found.")
            
            # --- Check if the loop is at the end of the list.
            # --- If true, break out of the program:
            if testing_loop_count == testing_list_length:
                print("No suitable image could be found.")
                break
            else:
                testing_loop_count += 1
                
    print(f"File testing.{extension} found.")


# --- Check that the file is the right size (1024 x 1024):
image = Image.open("test.png")
print(image.size[0], image.size[0])
    

# --- Load the list of app icon file sizes to a list or dictionaries:
try:
    with open(Path(APP_DIR, "image-sizes.json"), "r") as file:
        app_icon_image_sizes = json.load(file)
except FileNotFoundError:
    print("json file not found.")
    raise FileNotFoundError

print(app_icon_image_sizes)


# --- Create the folder to export the icons to:
try:
    Path.mkdir(EXPORT_DIR_PATH)
except FileExistsError:
    pass

print("test123")


# --- Resize the file and save it for each one that is in the JSON file:
for entry in app_icon_image_sizes:
    im = image.resize(size = (entry["width"],entry["height"]))
    #image.thumbnail(size = (entry["width"],entry["height"]))
    print(im)
    filename = f'AppIcon-{entry["device"]}-{entry["pt"]}@{entry["multiplier"]}x.png'
    
    im.save(Path(EXPORT_DIR_PATH, filename), "png")
    
    print(f"Exporing file {filename}.")