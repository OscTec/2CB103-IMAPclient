# Imports IMAPClient library
from imapclient import IMAPClient
# Imports email library
import email
HOST = 'elwood.yorkdc.net'
USERNAME = ''
PASSWORD = ''
ssl = False


# This method is used to sign in quickly with preset login details
def auto():
    userName = 'oscar.reid'
    password = 'W3B8KRKD'
    server.login(userName, password)
    server.select_folder("inbox", readonly=False)
    print("Logged in with default username and password")


# This method creates a folder after asking for a name for it from the user
def createFolder():
    print("Enter name of new folder")
    folderName = input(": ")
    server.create_folder(folderName)
    print("Created " + folderName)


# Method to rename a folder
def renameFolder():
    print("Enter name of folder you want to rename")
    folderName = input(": ")
    print("Enter name of folder you want to rename")
    newFolderName = input(": ")
    server.rename_folder(folderName, newFolderName)
    print(folderName + " has been renamed to " + newFolderName)


# Method to delete a folder
def deleteFolder():
    print("Enter name of folder you wish to delete")
    folderName = input(": ")
    server.delete_folder(folderName)
    print("Deleted " + folderName)


# Method to delete a email
def deleteemail():
    print("Enter ID of email you want to delete")
    emailID = input(": ")
    server.delete_messages(emailID)
    print("Deleted " + emailID)


# Method to select a folder
def selectFolder():
    print("Enter name of folder you want to select")
    folderName = input(": ")
    server.select_folder(folderName, readonly=False)
    print(folderName + " selected")


# Prints the save text file to the terminal
def read():
    file = open("savedEmails.txt", "r")
    print(file.read())


# Prints the following details about the folder MESSAGES, RECENT, UIDNEXT, UIDVALIDITY, UNSEEN
def status():
    print("Enter name of folder to check status")
    folderName = input(": ")
    print(server.folder_status(folderName, what=None))


# Method to copy a email from one folder to another
def copy():
    print("Enter ID of message you want to copy")
    messageID = input(": ")
    print("Enter name of folder you want to copy to")
    folderName = input(": ")
    server.copy(messageID, folderName)
    print(messageID + " copied to " + folderName)


# Prints a emails ID, FLAGS, FROM, DATE, SUBJECT and BODY
def fetch():
    messages = server.search(['NOT', 'DELETED'])
    response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE', 'RFC822'])
    for msgid, data in response.items():
        # print((msgid, data[b'RFC822.SIZE'], data[b'FLAGS'], data[b'RFC822']))
        emails = email.message_from_string(data[b'RFC822'].decode("utf8"))
        print("ID: " + str(msgid))
        print("Flags: " + str(data[b'FLAGS']).replace("',)", "").replace("(b'\\", ""))
        # print("Flags: " + str(data[b'FLAGS']))
        print("From: " + emails['From'])
        print("Date: " + emails['DATE'])
        print("Subject: " + emails['Subject'])
        for stuff in emails.walk():
            if stuff.get_content_type() == 'multipart':
                continue
            content_type = stuff.get_content_type()
            if "plain" in content_type:
                # print("Body ")
                # print(stuff.get_payload(decode=True))
                print("Body: " + str(stuff.get_payload(decode=True)).replace("b'", "").replace("\r", "").replace("\n", ""))
        print("")


# Method to save a email for offline reading
def save():
    try:
        messages = server.search(['NOT', 'DELETED'])
        response = server.fetch(messages, ['FLAGS', 'RFC822.SIZE', 'RFC822'])
        file = open("savedEmails.txt", "w")
        for msgid, data in response.items():
            # print((msgid, data[b'RFC822.SIZE'], data[b'FLAGS'], data[b'RFC822']))
            emails = email.message_from_string(data[b'RFC822'].decode("utf8"))
            ID = ("ID: " + str(msgid))
            Flag = ("Flags: " + str(data[b'FLAGS']).replace("',)", "").replace("(b'\\", ""))
            From = ("From: " + emails['From'])
            Date = ("Date: " + emails['DATE'])
            Subject = ("Subject: " + emails['Subject'])
            for stuff in emails.walk():
                if stuff.get_content_type() == 'multipart':
                    continue
                content_type = stuff.get_content_type()
                if "plain" in content_type:
                    # print("Body ")
                    # print(stuff.get_payload(decode=True))
                    Content = ("Body: " + str(stuff.get_payload(decode=True)).replace("b'", "").replace("\r", "").replace("\n", ""))
            file.write(str(ID + '\n' + Flag + '\n' + From + '\n' + Date + '\n' + Subject + '\n' + Content + '\n\n'))
    finally:
        file.close


# Method for listing all email ID numbers in a folder
def search():
    mailID = server.search([u'ALL'], None)
    print(mailID)


# Method that logs the user out of the server
def logout():
    server.logout()
    active = False
    print("Logged out")


# Method to check if a folder exists
def exist():
    print("Please enter name of folder you want to check exists")
    user_input = input(": ")
    print(server.folder_exists(user_input))


# Method that lists all folders
def listFolders():
    print(str(server.list_folders()).replace("b'/',", "").replace("b'\\", ""))
    # print(str(server.list_folders()))


# Method that asks user for login details then logs them in
def login():
    print("Enter your username")
    userName = str(input(": "))
    print("Enter your password")
    password = str(input(": "))
    try:
        server.login(userName, password)
        server.select_folder("inbox", readonly=False)
        print("You have logged in")
    # If details are incorrect error will be caught
    except Exception as LoginError:
        print("Failed login")


# Method to check how many emails are in a folder
def messages():
    print("Enter name of folder you want to know current number of mail in it")
    folder = input(": ")
    select_info = server.select_folder(folder)
    print('%d messages in INBOX' % select_info[b'EXISTS'])


while True:
    print("Enter start or quit")  # So you know the program is ready to use
    user_firstInput = input(": ")  # Ready for a user input to start or quit the program
    if user_firstInput == "start":  # The command to start the server
        # server = IMAPClient(HOST, use_uid=True, ssl=ssl)  # Used for automatically connecting to elwood.yorkdc.net
        print("Please enter host name")  # Asks for the host address
        user_host = input(": ")
        try:  # Try and except so program closes gracefully is user's inputted host is incorrrect
            server = IMAPClient(user_host, use_uid=True, ssl=ssl)
        except Exception as getaddrinfo:
            print("Host incorrect")
            break
        print("login or quit?")
        user_secondInput = input(": ")
        if user_secondInput == "login":
            login()  # Calls method to login using user inputted values
            # auto()  # Calls method to login with default details
            while True:  # While try means it will keep looping till user logs out
                print("Ready for further commands")
                user_input = input(": ")
                if user_input == "fetch":
                    fetch()

                elif user_input == "message":
                    messages()

                elif user_input == "create":
                    createFolder()

                elif user_input == "renamefolder":
                    renameFolder()

                elif user_input == "deletefolder":
                    deleteFolder()

                elif user_input == "copy":
                    copy()

                elif user_input == "delete":
                    deleteemail()

                elif user_input == "selectfolder":
                    selectFolder()

                elif user_input == "search":
                    search()

                elif user_input == "listfolders":
                    listFolders()

                elif user_input == "exist":
                    exist()

                elif user_input == "status":
                    status()

                elif user_input == "read":
                    read()

                elif user_input == "save":
                    save()

                elif user_input == "logoff":
                    logout()
                    break

                elif user_input == "logout":
                    logout()
                    break

                else:
                    print("Unknown input try something else")

        elif user_secondInput == "quit":
            break

        elif user_secondInput == "offline":
            read()

        else:
            print("Unknown input try something else")

    elif user_firstInput == "quit":
        break

    else:
        print("Unknown input try something else")
