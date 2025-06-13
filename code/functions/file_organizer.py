import shutil
import os
import glob

def move_file(origin_directory, destiny_directory, file_extension):
    
    pattern = os.path.join(origin_directory, f"*.{file_extension}")
    
    
    files = glob.glob(pattern)
    
    for file in files:
        file_name = os.path.basename(file)
        destiny_path = os.path.join(destiny_directory, file_name)
        
        
        try:
            shutil.move(file, destiny_path)
            print(f"Moved {file_name} to {destiny_directory}")
        except Exception as e:
            print(f"Error moving {file_name}: {e}")
            
            

def copy_files(origin_directory, destiny_directory, file_extension):
    
    pattern = os.path.join(origin_directory, f"*.{file_extension}")
    
    
    files = glob.glob(pattern)
    
    for file in files:
        file_name = os.path.basename(file)
        destiny_path = os.path.join(destiny_directory, file_name)
        destiny_file_path = os.path.join(destiny_directory, file_name)

        if not os.path.exists(destiny_file_path):        
            try:
                shutil.copy(file, destiny_path)
                print(f"{file_name} copied to {destiny_directory}")
            except Exception as e:
                print(f"Error copying {file_name}: {e}")
        else:
            print(f"{file_name} already exists in {destiny_directory}, skipping copy.")

def delete_files(directory_origin, directory_destiny, file_extension):
    # Deletes files from directory_destiny that are not present in directory_origin
    pattern = os.path.join(directory_destiny, f"*.{file_extension}")
    files_destiny = glob.glob(pattern)
    for file in files_destiny:
        file_name = os.path.basename(file)
        origin_file_path = os.path.join(directory_origin, file_name)
        
        if not os.path.exists(origin_file_path):
            try:
                os.remove(file)
                print(f"Deleted {file_name} from {directory_destiny}")
            except Exception as e:
                print(f"Error deleting {file_name}: {e}")