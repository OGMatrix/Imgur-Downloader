# Imports
import argparse
from genericpath import exists
from colorama import Fore, Back, Style
import requests
from clint.textui import progress
from PIL import Image
from os import path
import os

# Argument Parser
parser = argparse.ArgumentParser("Image")
parser.add_argument("url", help="Imgur URL to download Image", type=str)
parser.add_argument("name", help="Name of the Image to Save", type=str)


# Arguments
args = parser.parse_args()


# Str
url  = str(args.url)
name = str(args.name)

if not url.startswith("https://i.imgur.com/"):
    print(Fore.BLACK + "[Downloader] " + Fore.RED + "Download Link doesnt starts with https://i.imgur.com/ !")
    exit()

if not path.exists("images"):
    print(Fore.BLACK + "[Downloader] " + Fore.RED + "'Images' Folder wasn't created yet, so created it for you!")
    os.mkdir("images")

# Script
print(Fore.BLACK + "[Downloader] " + Fore.CYAN + "Fetching Image... " + Fore.GREEN + f"[{args.url}]")
print("   ")

# Request Image
response = requests.get(args.url, stream=True)
path = "./images/" + args.name + ".jpg"

print(Fore.BLACK + "[Downloader] " + Fore.BLUE + "Fetched Image, now starting download... " + Fore.GREEN + f"[{args.url}]")
print(" ")
print(Fore.WHITE)

# Progess Bar
with open(path, 'wb') as f:
    total_length = int(response.headers.get('content-length'))
    for chunk in progress.bar(response.iter_content(chunk_size=1024), expected_size=(total_length/1024) + 1): 
        if chunk:
            f.write(chunk)
            f.flush()

print(" ")
print(Fore.BLACK + "[Downloader] " + Fore.BLUE + "Download Finished! " + Fore.GREEN + f"[{args.url}]")

img = Image.open(path)
img.show(args.name)

print(Fore.RESET)