import os
import platform
import subprocess
import datetime

# Ask for database name
database_name = input("Enter database name: ")
os_name = platform.system()
# Ask for username and password
username = 'root'

# Set the path of the backup file
backup_file = os.path.join(os.getcwd(), f"{database_name}_{datetime.date.today()}.sql")

# Set the mysqldump command based on the OS type
if  os_name.lower() == "windows":
    mysqldump_cmd = "C:\\Program Files\\MySQL\\MySQL Server 8.0\\bin\\mysqldump.exe"
else:
    mysqldump_cmd = "mysqldump"

# Run the mysqldump command to create the backup
subprocess.run([
    mysqldump_cmd,
    "--single-transaction",
    "--routines",
    "--triggers",
    "--events",
    "--default-character-set",
    "utf8",
    "--add-drop-database",
    "--add-drop-table",
    "--create-options",
    "--databases",
    database_name,
    "--user",
    username,
    "--password",
    
    "--result-file",
    backup_file
])