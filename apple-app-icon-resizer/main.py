# --- Import the required libraries:
import json
import os

from pathlib import Path
from PIL import Image


# --- Define constants and variables:
APP_DIR = Path(__file__).resolve().parent
EXPORT_DIR = ""
# print(WORKING_DIR)

file_name = "app-icon"
file_extensions = ["jpg", "jpeg", "png"]
file_found = False

image_file_sizes_list = "image-sizes.json"


# --- Check for the presence of the app-icon image:
for extension in file_extensions:
    print(extension)


# --- Load the list of app icon file sizes to a list or dictionaries:
with open("image-sizes.json", "r") as file:
    app_icon_image_sizes = json.load(file)

print(app_icon_image_sizes)


# --- Check that the file is the right size (1024 x 1024):
image = Image.open("test.png")
print(image.size[0], image.size[0])


# --- Resize the file and save it for each one that is in the JSON file:
# image.thumbnail(size = (500,500))
# image.save("test1.png", "png")
