import os


from functions import file_organizer as move


# Local variables
localdirectory = ""
newtolocaldirectory = ""


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
            elif "remotedirectory1" in line:
                remotedirectory1 = line.split("=")[1].strip()
            elif "remotedirectory2" in line:
                remotedirectory2 = line.split("=")[1].strip()
except FileNotFoundError:
    print("Configuration file 'config.ini' not found. Please create it with the required settings.")
    exit(1)
finally:
    if not localdirectory or not newtolocaldirectory or not remotedirectory1 or not remotedirectory2:
        print("Incomplete configuration. Please ensure all settings are provided in 'config.ini'.")
        exit(1)

#* Copy files from remote1 to localdirectory

if os.path.exists(remotedirectory1):
    move.copy_files(remotedirectory1, localdirectory)
    move.delete_files(remotedirectory1, localdirectory, "mp3")
else:
    print(f"Remote directory {remotedirectory1} does not exist. Skipping copy operation.")

#* Copy files from remote2 to localdirectory
if os.path.exists(remotedirectory2):
    move.copy_files(remotedirectory2, localdirectory)
    move.delete_files(remotedirectory2, localdirectory, "mp3")
else:
    print(f"Remote directory {remotedirectory2} does not exist. Skipping copy operation.")