import os
# install glob using: `pip install glob2`
import glob

# declaring the global variables
version_control_folder = "version control"
file_extension = ".py"

# check if a folder called "version control" exits. If not, create the folder before proceeding
if not (os.path.isdir(version_control_folder)):
    os.mkdir(version_control_folder)

# check for files with a particular file extension in the current directory
for file in glob.glob(f"*{file_extension}"):
    # if the file found is not the current file (auto_version_control.py), then proceed
    if not (file == os.path.basename(__file__)):
        file_without_extension = file.split(".")[0]
        # create a folder for each file found earlier if the folder does not exist
        # if "main.py" was found earlier, create a folder named "main"
        if not (os.path.isdir(f'{version_control_folder}/{file_without_extension}')):
            os.mkdir(f'{version_control_folder}/{file_without_extension}')

        no_of_files = len(os.listdir(f'{version_control_folder}/{file_without_extension}'))
        f1 = open(f"{file_without_extension}{file_extension}", "r")
        # create a text file and write it line-by-line
        with open(f'{version_control_folder}/{file_without_extension}/{file_without_extension}v{no_of_files + 1}.0.txt',
                  'w') as f:
            for line in f1:
                f.write(line)

# used to show that the file is meant to be executed
if __name__ == "__main__":
    pass
