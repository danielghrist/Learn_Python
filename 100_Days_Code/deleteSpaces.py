'''
Script to run through directories in current direcory and delete and spaces in the directory name.
'''

import os
from pathlib import Path

# Testing how os works to obtain the Current Working Directy Using os Module:
# cwd = os.getcwd()
# print()
# print(f"CWD: {cwd}")
# print(type(cwd))

# Testing how pathlib works with Current Working Directy Using pathlib Module and Path Object:
# script_path = Path(__file__, "../").resolve()
# print(f"Script Path: {script_path}")
# print(f"Script Path Using using pathlib Path: {script_path}")

# print(Path(__file__, "../../").resolve())
# print()

# Print out all the top level directy names in the current folder that the script is in:
# Get path to directory/folder that the script is in using pathlib:
file_directory = Path(__file__, "../").resolve()
print(file_directory)  # Print the file directory the script is in:

# Loop through the file_directory and print out each directory:
dir_list = os.listdir(file_directory)
# dir_list.sort()
# print(dir_list)

for dir_name in dir_list:
    curr_dir = os.path.join(file_directory, dir_name)
    if os.path.isdir(curr_dir):
        renamed_folder = curr_dir.replace(" ", "")
        # print(curr_dir)
        # print(renamed_folder)
        os.rename(curr_dir, renamed_folder)
        print(f"{curr_dir} is being renamed to:\n{renamed_folder}")
