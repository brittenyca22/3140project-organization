from pathlib import Path
import os, shutil, send2trash

downloads_path = Path.home() / 'Downloads' # Reference to Downloads folder


#This part is pretty much optional, but I am showing you how to create folders using Python
while True:

    # Create the folder
    folderName = input("Enter a folder name (blank to stop): ") # Enter a folder name
    if folderName == '':
        break
    
    target_folder = downloads_path / folderName # Reference to the target folder


    if target_folder.exists(): # Check if the files exists.
        print('This folder already exists.') 
        continue 
    else:
        target_folder.mkdir() # Creates folder if it does not exist already
        print(f"Folder created at: {target_folder}")
        continue

#Move existing files into created folders
for filename in os.listdir(downloads_path): # Loop through the entire Downloads folder
    
    full_path = downloads_path / filename
    if full_path.is_file() and filename.endswith('.pdf'):
        os.makedirs('C:/Users/britt/Downloads/PDFs', exist_ok=True) # Prevents shutil from creating a .file file and overwriting my existing files.
        shutil.move(full_path, 'C:/Users/britt/Downloads/PDFs')
    elif filename.endswith('.exe'):
        os.makedirs('C:/Users/britt/Downloads/Applications', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Applications')
    elif filename.endswith('.jpg'):
        os.makedirs('C:/Users/britt/Downloads/Images', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Images')
    elif filename.endswith('.png'):
        os.makedirs('C:/Users/britt/Downloads/Images', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Images')
    elif filename.endswith('.jpeg'):
        os.makedirs('C:/Users/britt/Downloads/Images', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Images')
    elif filename.endswith('.docx'):
        os.makedirs('C:/Users/britt/Downloads/PDFs', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Word Documents')
    elif filename.endswith('.doc'):
        os.makedirs('C:/Users/britt/Downloads/PDFs', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Word Documents')
    elif filename.endswith('.zip'):
        os.makedirs('C:/Users/britt/Downloads/Zip Files', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Zip Files')
    elif filename.endswith('.txt'):
        os.makedirs('C:/Users/britt/Downloads/Text Documents', exist_ok=True)
        shutil.move(full_path, 'C:/Users/britt/Downloads/Text Documents')
    elif full_path.is_dir(): # Print message if file is a folder.
        print(f' {filename} is a folder.')
    else:
        print(f'Skipped: {filename} (no matching folder)')


# Handles duplicate files and unrecognized files.
    file_list = os.listdir(downloads_path)
    allowed_exts = ['.zip', '.png', '.jpg', '.jpeg', '.doc','.docx', '.pdf', '.exe']

for i in range(len(file_list)):
    filename = file_list[i]
    full_path_1 = downloads_path / filename

    for j in range(i + 1, len(file_list)):  # Prevents self-comparison by iterating through filename
        dupliFile = file_list[j]
        full_path_2 = downloads_path / dupliFile

        ext1 = full_path_1.suffix.lower() # Extracts the file extensions of files in Downloads and deals with capitalization sensitivities.
        ext2 = full_path_2.suffix.lower()

        if (
            full_path_1.is_file()
            and full_path_2.is_file()
            and ext1 in allowed_exts # Prevents premission errors for files not specified in allowed_exts
            and ext2 in allowed_exts
            and full_path_1.read_bytes() == full_path_2.read_bytes()
            ):
                send2trash.send2trash(full_path_2) # Safely delete file if duplicate exists
                print(f"Duplicate deleted: {dupliFile}")
        
