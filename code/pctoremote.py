import os

from functions import file_organizer as move


# Local variables
localdirectory = ""
newtolocaldirectory = ""

# Remote variables
remote1 = ""
remote2 = ""

# Remote directories
remotedirectory1 = ""
remotedirectory2 = ""


# Configuration values
#noremote1 = ""

#

ruta_config = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.ini'))


try:
    with open(ruta_config, "r") as file:
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


# print(localdirectory)
# print(newtolocaldirectory)
# print(remote1)
# print(remote2)
# print(remotedirectory1)
# print(remotedirectory2)


# Moves files from newtolocaldirectory to localdirectory

try:
    move.move_file(newtolocaldirectory, localdirectory, "mp3")
except Exception as e:
    print(f"Error moving files from {newtolocaldirectory} to {localdirectory}: {e}")


# Copies files from localdirectory to remote directories.
# And deletes them from remote directories if they do not exist in localdirectory

# Checks if remote directories are available
if not os.path.exists(remotedirectory1):
    print(f"Remote directory {remotedirectory1} does not exist. Please check the device and configuration.")
#    remote=1
else:
    move.copy_files(localdirectory, remotedirectory1, "mp3")
    move.delete_files(localdirectory, remotedirectory1, "mp3")

if not os.path.exists(remotedirectory2):
    print(f"Remote directory {remotedirectory2} does not exist. Please check the device and configuration.")
#    remote=2
else:
    move.copy_files(localdirectory, remotedirectory2, "mp3")
    move.delete_files(localdirectory, remotedirectory2, "mp3")
