import os

userfile = input("Name your File or Choose your file \n")
WriteReadDelete = input("W to write file, R to read file,D to delete file")
if ".txt" not in userfile:
    userfile = userfile + ".txt"
if WriteReadDelete.lower () == "w":
    file = open(userfile, "x")
    data = input("Write your file \n")
    file.write(data)
    file.close()
elif WriteReadDelete.lower() == "r":
    file = open(userfile, "r")
    data = file.read()
    print(data)
    file.close()
elif WriteReadDelete.lower() == "d":
    sure = input("Are you sure you want to delete your file? Yes or No")
    if sure.lower == "yes":
        os.remove(userfile)
