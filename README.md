This is the read me for IMAPclient.

Launch the program by typing "python imapclient.py" into the
console when in the folder that the file is in.

This then allows you to start entering commands into the console.
After running the program you will be prompted to enter start.
It will then ask for the host address you want to connect to.
It will then ask you to login or quit.
If you enter login it will the ask for a username and password.
If entered correctly you will then be able to use the following commands.
INBOX is automatically selected.

List of commands:

logoff or logout - This logs the user out of the server.

quit - This closes the program. You must use logout or logoff first.

auto - This logs in with programmers details

fetch - This display the internal date and flags for each mail in current folder

message - Prompts user for folder name. It then prints how many emails are in that folder

create - This prompts the user for to name the new folder then it says
"Created folderName"

renamefolder - This asks the user which folder they would like to rename and what they want
to rename it to. Then prints "folderName has been renamed to newFolderName".

deletefolder - Prompts the user for which folder they want to delete then prints
"Deleted folderName".

delete - Prompts the user for a ID of email in current folder. They deletes the email and
prints "Deleted emailID"

copy - This prompts the user for which email they wants to copy by ID
then asks for which folder to copy it to. Then prints "messageID copied to folderName".

selectfolder - This prompts the user for which folder they want to use. Then
prints "folderName selected".

listfolders - Lists all folders.

exist - Prompts user for a name of a folder. Prints True or False depending on
if the folder exists or not

status - Prompts the user to enter a name of a folder. Prints the status
of the folder.

save - Downloads the details of all emails in currently selected folder.

read - Prints the details of all downloaded emails.  

search - prints the ID numbers of emails in selected folder.  
