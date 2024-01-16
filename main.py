from inc.proses import convert_to_mp3, browse_paths
from assets.logo import LOGO
import os
import time

if __name__ == "__main__":

    os.system("cls" if os.name == "nt" else "clear")
    time.sleep(2)
    print(LOGO)
    time.sleep(1)
    selected_input = browse_paths()


    os.system("cls" if os.name == "nt" else "clear")
    if not selected_input:
        print("No valid input selected. Exiting.")
    else:
        directory = "MP3"
        os.makedirs(directory, exist_ok=True)
        output_directory_path = directory
        convert_to_mp3(selected_input["path"], output_directory_path)


    
