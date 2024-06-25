import os
import shutil
import argparse
#Creating def function
def sort_files_on_desktop(desktop_path):
    folder_names = {
        ".txt": "Text Files",
        ".pdf": "PDF Files",
        ".docx": "Word Files",
        ".ppt": "PowerPoint Files",
        ".pptx": "PowerPoint Files",
        ".csv": "Excel Files",
        ".xlsx": "Excel Files",
        ".xls": "Excel Files",
        ".png": "PNG Files",
        ".jpeg": "JPEG Files",
        ".jpg": "JPG Files",
        ".rar": "RAR Files",
        ".zip": "Zip Files",
        ".7z": "7Z Files",
        ".exe": "Executables",
        ".ps1": "Powershell Scripts",
        ".py": "Python Scripts",
        ".card": "Evolis Samples",
    }
#Making it loop each file on desktop
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)

        if os.path.isfile(file_path):
            file_extension = os.path.splitext(file_name)[1].lower()

            if file_extension in folder_names:
                folder_name = folder_names[file_extension]

                folder_path = os.path.join(desktop_path, folder_name)

                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)

                new_file_path = os.path.join(folder_path, file_name)
                shutil.move(file_path, new_file_path)
#Creating parser argparse
def main():
    parser = argparse.ArgumentParser(description='Sort Files into folders according to their file type(Extension)')
    parser.add_argument('--desktop_path', type=str, help="The path to desktop")
    args = parser.parse_args()

    desktop_path = args.desktop_path

    if desktop_path:
        sort_files_on_desktop(desktop_path)
        print("Files were sorted")
    else:
        print("Please provide the valid Desktop path")

if __name__ == "__main__":
    main()
