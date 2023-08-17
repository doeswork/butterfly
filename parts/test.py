print("Hello")

import subprocess

git_command = "git status"

output = subprocess.check_output(git_command, shell=True, text=True)
print(output)

