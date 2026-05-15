## Project --->>> { CURD  OPERATION }

"""try
   except"""

from pathlib import Path
import os

def readfileandfolder():
    try:
        P = Path("")
        items = list(P.rglob("*"))
        for index,file in enumerate(items):
            print(f"{index} - {file}")
    except Exception as e:
        print(e)


def create_file():
    #/Users/raviprakash/Desktop/project/File handling/main.py
    try:
        file_name = input("enter name of your file :")
        P = Path(file_name)
        if P.exists():
            print("FILE ALREADY EXISTS")
        else:
            with open(file_name ,"w") as file:
                content = input("enter your content in file : ")
                file.write(content)
                print("FILE ADDED !")
    except Exception as e:
        print(e)


def read_file():
    try:
        readfileandfolder()
        file_name = input("enter name of your file :")
        P = Path(file_name)
        if P.exists():
            with open(file_name,"r") as file:
                print(file.read())
        else:
            print("FILE NOT FOUND !")
    except Exception as e:
        print(e)



def update_file():
    try:
        readfileandfolder()
        file_name = input("enter name of file :")
        P = Path(file_name)
        if P.exists():
            print("press 1 to overwrite the content")
            print("press 2 to append new content")

            option = int(input("enter your choice for updating a file : "))
            if option == 1:
                with open(file_name,"w") as file:
                    content = input("enter your content :")
                    file.write(content)
                    print("CONTENT CHANGED")

            elif option == 2:
                with open(file_name,"a") as file:
                    content = input("enter your content :")
                    file.write(content)
                    print("CONTENT CHANGED")
            else:
                print("INVALID INPUT")
        else:
            print("FILE DOES NOT EXISTS")
    except Exception as e:
        print(e)


def delete_file():
    try:
        readfileandfolder()
        file_name = input("enter name of file :")
        P = Path(file_name)
        if P.exists():
            os.remove(P) # os is removing path of that file completely for the system.
            print("FILE DELETED")
    except Exception as e:
        print(e)       


def rename_file():
    readfileandfolder()
    file_name = input("enter name of your file:")
    p = Path(file_name)
    if p.exists():
        new_file = input("enter new name of your file:")
        p.rename(new_file)
        print("file renamed !")
    else:
        print("file not found !")


def create_folder():
    readfileandfolder()
    folder_name = input("enter name of your folder :")
    p = Path(folder_name)
    if p.exists():
        print("folder already exist !")
    else:
        p.mkdir()   # make directory
        print("FOLDER CREATED !")


def delete_folder():
    readfileandfolder()
    folder_name = input("enter name of your folder :")
    p = Path(folder_name)
    if p.exists():
        p.rmdir()
        print("folder deleted !")
    else:
        print("folder not found ")


def create_file_in_folder():
    try:
        folder_name = input("enter name of your folder :")
        file_name = input("enter name of your file :")
        p = Path(folder_name/file_name)
        if p.exists():
            print('file already exist')
        else:
            p.mkdir()
            print("created successfully");
            with open(file_name,"w") as file:
                content = input("enter your file content:")
                file.write(content)
                print("created sucessfully")
    except Exception as e:
        print(e)
        



while True:
    print("press 1 for creaeting a file ")
    print("press 2 for reading a file ")
    print("press 3 for updating a file")
    print("press 4 for deleting a file")
    print("press 5 for rename file ")
    print("press 6 for creating a folder")
    print("print 7 for deleting a folder ")
    print("press 0 to exit a file ")

    option = int(input("enter your choice : "))
    if option == 1:
        create_file()

    if option == 2:
        read_file()

    if option == 3:
        update_file()

    if option == 4:
        delete_file()

    if option == 5:
        rename_file()
    
    if option == 6:
        create_folder()

    if option == 7:
        delete_folder()

    if option == 0:
        break
