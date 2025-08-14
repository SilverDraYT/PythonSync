import os

from configobj import ConfigObj
from pathlib import Path
from mycode.functions import file_organizer as move
from mycode.functions import logfile_management as logmanagement

def remotetopcfunction():
    #! Read .ini file

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

    #! Copy files from remote1 to localdirectory
    for directory in values:

        if os.path.exists(directory):
            list_copyfiles = move.copy_files(directory, localdirectory, "mp3", 0)
            list_deletefiles = move.delete_files(directory, localdirectory, "mp3")

            # Log the copied and deleted files
            logmanagement.file_write(list_copyfiles, list_deletefiles, localdirectory)
        else:
            print(f"Remote directory {directory} does not exist. Skipping copy operation.")

