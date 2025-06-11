import shutil
import os
import glob

def move_file(origin_directory, destiny_directory, file_extension):
    
    pattern = os.path.join(origin_directory, f"*.{file_extension}")
    
    print (pattern)
    
    files = glob.glob(pattern)
    
    for file in files:
        file_name = os.path.basename(file)
        destiny_path = os.path.join(destiny_directory, file_name)
        
        
        try:
            shutil.move(file, destiny_path)
            print(f"Moved {file_name} to {destiny_directory}")
        except Exception as e:
            print(f"Error moving {file_name}: {e}")
            
            
            