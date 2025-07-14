import os
import configparser

from functions import file_organizer as move
from functions import logfile_management as logmanagement

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


# * Copy files from remote1 to localdirectory

if os.path.exists(remotedirectory1):
    list_copyfiles=move.copy_files(remotedirectory1, localdirectory, "mp3", 0)
    list_deletefiles=move.delete_files(remotedirectory1, localdirectory, "mp3")

    # Log the copied and deleted files
    logmanagement.file_write(list_copyfiles, list_deletefiles, localdirectory)
else:
    print(f"Remote directory {remotedirectory1} does not exist. Skipping copy operation.")

# * Copy files from remote2 to localdirectory
if os.path.exists(remotedirectory2):
    list_copyfiles=move.copy_files(remotedirectory2, localdirectory, "mp3", 0)
    list_deletefiles=move.delete_files(remotedirectory2, localdirectory, "mp3")

    # Log the copied and deleted files
    logmanagement.file_write(list_copyfiles, list_deletefiles, localdirectory)
else:
    print(f"Remote directory {remotedirectory2} does not exist. Skipping copy operation.")
