import os
import configparser

from functions import file_organizer as move


# Local variables
localdirectory = ""
newtolocaldirectory = ""


# Remote directories
remotedirectory1 = ""
remotedirectory2 = ""



config = configparser.ConfigParser()

try:
    
    config.read("config.ini")
    
    localdirectory = config.get("Local_variables", "localdirectory", fallback="")
    newtolocaldirectory = config.get("Local_variables", "newtolocal", fallback="")
    remotedirectory1 = config.get("Remote_variables", "remotedirectory1", fallback="")
    remotedirectory2 = config.get("Remote_variables", "remotedirectory2", fallback="")
except configparser.Error as e:
    print("Configuration file 'config.ini' not found. Please create it with the required settings.")
    exit(1)
finally:
    if not localdirectory or not newtolocaldirectory or not remotedirectory1 or not remotedirectory2:
        print("Incomplete configuration. Please ensure all settings are provided in 'config.ini'.")
        exit(1)


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
