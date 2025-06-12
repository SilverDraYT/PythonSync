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