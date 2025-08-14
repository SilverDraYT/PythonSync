import os

from configobj import ConfigObj
from pathlib import Path
from mycode.functions import file_organizer as move
from mycode.functions import logfile_management as logmanagement

#! Read .ini file
def pctoremotefunction():
    find_config = Path(__file__).resolve().parents[1] / 'config.ini'

    config = ConfigObj(str(find_config), encoding='UTF8')

    namelist = list(config["Remote_variables"].keys())

    values = [config["Remote_variables"][key] for key in namelist]

    #! Local variables
    localdirectory = ""
    newtolocaldirectory = ""



    #! Give the values to local variables
    try:
        local_vars = config.get("Local_variables", {})
        newtolocaldirectory = local_vars.get("newtolocal", "")
        localdirectory = local_vars.get("localdirectory", "")
    except Exception as e:
        print("Configuration file 'config.ini' not found or invalid. Please create it with the required settings.")
        exit(1)
    finally:
        if not localdirectory or not newtolocaldirectory:
            print("Incomplete configuration. Please ensure all settings are provided in 'config.ini'.")
            return


    #! Move the files from newtolocaldirectory to localdirectory
    try:
        move.move_file(newtolocaldirectory, localdirectory, "mp3")
    except Exception as e:
        print(f"Error moving files from {newtolocaldirectory} to {localdirectory}: {e}")


    #! Copies files from localdirectory to remote directories.
    #! And deletes them from remote directories if they do not exist in localdirectory
    for directory in values:
        print(f"Processing remote directory: {directory}")
        # Checks if remote directories are available
        if not os.path.exists(directory):
            print(f"Remote directory {directory} does not exist. Please check the device and configuration.")
        #    remote=1
        else:
            list_copyfiles=move.copy_files(localdirectory, directory, "mp3", 1)
            list_deletefiles=move.delete_files(localdirectory, directory, "mp3")

            # Log the copied and deleted files
            logmanagement.file_write(list_copyfiles, list_deletefiles, directory)

