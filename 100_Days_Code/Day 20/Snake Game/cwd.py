'''
Short script testing out different ways to obtain the current directory of the file so I don't keep getting "File does not exist" when trying to open files in the Snake Game.
'''

import os
from pathlib import Path

# Obtain the Current Working Directy Using os Module:
cwd = os.getcwd()
print(f"CWD: {cwd}")
print(type(cwd))

# Obtain the Current Working Directy Using pathlib Module and Path Object:
script_path = Path(__file__, "../").resolve()
print(f"Script Path: {script_path}")
print(f"Script Path Using .joinpath: {script_path.joinpath('highscores.txt')}")

print(Path(__file__, "../").resolve())
