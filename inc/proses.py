import os
from moviepy.editor import VideoFileClip
from tkinter import Tk, filedialog

def convert_to_mp3(input_path, output_directory):
    try:
        input_path = os.path.abspath(input_path)

        if os.path.isdir(input_path):
            # If input is a folder, process all video files inside the folder

            # Create a new folder in the output directory based on the uploaded folder name
            folder_name = os.path.basename(input_path)
            output_folder_path = os.path.join(output_directory, folder_name)
            os.makedirs(output_folder_path, exist_ok=True)

            for filename in os.listdir(input_path):
                if filename.endswith(".mp4"):
                    video_file_path = os.path.join(input_path, filename)
                    process_video_file(video_file_path, output_folder_path)

        elif os.path.isfile(input_path) and input_path.endswith(".mp4"):
            # If input is a single video file, process that file

            # Output directly to the specified output directory
            output_folder_path = output_directory
            process_video_file(input_path, output_folder_path)
            
        else:
            print(f"Invalid input: {input_path}. Skipping.")

    except Exception as e:
        print(f"Error: {e}")

def process_video_file(input_file, output_directory):
    try:
        video_clip = VideoFileClip(input_file)
        audio_clip = video_clip.audio
        
        filename_without_extension = os.path.splitext(os.path.basename(input_file))[0]

        output_file_path = os.path.join(output_directory, f"{filename_without_extension}.mp3")

        audio_clip.write_audiofile(output_file_path, codec='mp3')

        print(f"Conversion successful!")

    except Exception as e:
        print(f"Error processing {input_file}: {e}")

def browse_paths():
    root = Tk()
    root.withdraw()

    print("Select an option:")
    print("1. Upload file(s)")
    print("2. Upload folder")

    option = input("Enter option number: ")

    if option == "1":
        # Memilih file individu
        paths = filedialog.askopenfilenames(title="Select video file(s)", filetypes=[("Video files", "*.mp4")], initialdir="/")
        return {"type": "file", "path": list(paths)[0]}
    elif option == "2":
        # Memilih folder
        folder_path = filedialog.askdirectory(title="Select a folder containing video files", initialdir="/")
        return {"type": "folder", "path": folder_path}
    else:
        print("Invalid option. Exiting.")
        return None

if __name__ == "__main__":
    selected_input = browse_paths()

    if not selected_input:
        print("No valid input selected. Exiting.")
    else:
        output_directory_path = r"E:\Fb Fanspage\Bahan\converter\mp3"
        convert_to_mp3(selected_input["path"], output_directory_path)
