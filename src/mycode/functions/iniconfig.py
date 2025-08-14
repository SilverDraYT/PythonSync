from configobj import ConfigObj
from pathlib import Path

find_config = Path(__file__).resolve().parents[2] / 'config.ini'

config = ConfigObj(str(find_config), encoding='UTF8') #Already reads the file

def addvariables(num_external): # Marks the max number if variables that has to exist
    namelist = list(config["Remote_variables"].keys())
    
    for i in range(num_external):
       var_name = f"remotedirectory{i+1}"
       
       if var_name not in namelist:
        config["Remote_variables"][var_name] = None
    
    config.write()    
    

def erasevariables(num_external): # Marks the max number if variables that has to exist
    namelist = list(config["Remote_variables"].keys())
    
    # Goes backwards till we have the right amount of variables
    for i in range(len(namelist), (num_external-1), -1): 
       var_name = f"remotedirectory{i+1}"
       
       if var_name in namelist:
        del config["Remote_variables"][var_name]
    
    config.write()
        



