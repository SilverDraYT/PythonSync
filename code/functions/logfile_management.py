import datetime
import os 


def file_write(copied_files, deleted_files, directory):
    
    # Creates an access to the logs directory
    logs_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "logs")
    os.makedirs(logs_dir, exist_ok=True)

    # Check if the file exists in the directory
    log_path = os.path.join(logs_dir, f"{datetime.date.today()}.txt")

    with open(log_path, "a", encoding="utf-8") as log:

        log.write("========================================\n")
        log.write(f"Log file for {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n")
        log.write(f"Moves to {directory}\n")
        log.write("---\n")

        for file in copied_files:
            log.write(f"Copied: {file}\n")

        for file in deleted_files:
            log.write(f"Deleted: {file}\n")

        log.write("---\n")
        log.write(f"Total copied files: {len(copied_files)}\n")
        log.write(f"Total deleted files: {len(deleted_files)}\n")
        log.write("========================================\n")
