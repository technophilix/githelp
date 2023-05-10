import os
import subprocess
from colorama import Fore, Back, Style
root_folder = os.curdir
action = input("Enter pull or push: ")

if action == "push":
    commit_message = input("Enter commit message: ")
# Loop through each folder in the root folder
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder)
        
        if os.path.isdir(folder_path) and os.path.exists(os.path.join(folder_path, ".git")):
            print(Fore.RED+"Working on project {}".format(folder))
            print(Style.RESET_ALL)
            # Change directory to the git project folder
            os.chdir(folder_path)

            # Run git add command
            subprocess.run(["git", "add", "."])

            # Run git commit command
            # commit_message = "Commit message"
            subprocess.run(["git", "commit", "-m", commit_message])

            # Run git push command
            subprocess.run(["git", "push", "-u", "origin", "master"])
            os.chdir('..')

else:
    for folder in os.listdir(root_folder):
        folder_path = os.path.join(root_folder, folder)
        if os.path.isdir(folder_path) and os.path.exists(os.path.join(folder_path, ".git")):
            # Change directory to the git project folder
            os.chdir(folder_path)

            # Run git add command
            subprocess.run(["git", "pull"])
