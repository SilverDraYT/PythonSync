import os
import shutil
import sys

import file_organaizer as move


# Local variables
localdirectory=""
newtolocaldirectory=""

# Remote variables
remote1=""
remote2=""

# Remote directories
remotedirectory1=""
remotedirectory2=""


# Configuration values
noremote1=""

try:
    with open("config.ini", "r") as file:
        for line in file:
            if "localdirectory" in line:
                localdirectory = line.split("=")[1].strip()
            elif "newtolocal" in line:
                newtolocaldirectory = line.split("=")[1].strip()
            elif "remote1" in line:
                remote1 = line.split("=")[1].strip()
            elif "remote2" in line:
                remote2 = line.split("=")[1].strip()
            elif "remotedirectory1" in line:
                remotedirectory1 = line.split("=")[1].strip()
            elif "remotedirectory2" in line:
                remotedirectory2 = line.split("=")[1].strip()
except FileNotFoundError:
    print("Configuration file 'config.ini' not found. Please create it with the required settings.")
    exit(1)
finally:
    if not localdirectory or not newtolocaldirectory or not remote1 or not remote2 or not remotedirectory1 or not remotedirectory2:
        print("Incomplete configuration. Please ensure all settings are provided in 'config.ini'.")
        exit(1)
        
print(localdirectory)
print(newtolocaldirectory)
print(remote1)
print(remote2)
print(remotedirectory1)
print(remotedirectory2)


# if os.path.exists(remotedirectory1) and os.path.exists(remotedirectory2):
#     remote=3

    
# if not remote:
#     remote=-1


move.move_file(newtolocaldirectory, localdirectory, "mp3")


#if os.path.exists(remotedirectory1) or os.path.exists(remotedirectory2):
    


# Checks if remote directories are available
if not os.path.exists(remotedirectory1):
    print(f"Remote directory {remotedirectory1} does not exist. Please check the device and configuration.")
#    remote=1
    
if not os.path.exists(remotedirectory2):
    print(f"Remote directory {remotedirectory2} does not exist. Please check the device and configuration.")
#    remote=2
    