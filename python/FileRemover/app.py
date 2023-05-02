# import os

# def enumerate_files(path):
#     for file in os.listdir(path):
#         file_path = os.path.join(path, file)
#         if os.path.isfile(file_path):
#             os.remove(file_path)
#             print(f"Removed file: {file_path}")
#         elif os.path.isdir(file_path):
#             enumerate_files(file_path)
#             if not os.listdir(file_path):
#                 os.rmdir(file_path)
#                 print(f"Removed directory: {file_path}")
#         else:
#             print("Something went wrong")

# def confirmation():
#     path = input("path >> ")
#     if not os.path.exists(path):
#         print("Path doesn't exist")
#         confirmation()
#         return
#     response = input(f"Are you sure?(Y/n) path: {path} >> ")
#     match response:
#         case "y": enumerate_files(path)
#         case "n": exit()
#         case _: exit()

# confirmation()

import os

def enumerate_files(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            os.remove(file_path)
            print(f"Removed file: {file_path}")
        elif os.path.isdir(file_path):
            enumerate_files(file_path)
            if not os.listdir(file_path):
                os.rmdir(file_path)
                print(f"Removed directory: {file_path}")
        else:
            print("Something went wrong")

def confirmation():
    path = input("path >> ")
    if not os.path.exists(path):
        print("Path doesn't exist")
        confirmation()
        return
    response = input(f"Are you sure?(Y/n) path: {path} >> ")
    match response:
        case "y":
            enumerate_files(path)
            os.rmdir(path)
            print(f"Removed top-level directory: {path}")
        case "Y":
            enumerate_files(path)
            os.rmdir(path)
            print(f"Removed top-level directory: {path}")
        case "n":
            exit()
        case _:
            exit()

confirmation()
