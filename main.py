
import os
import shutil
import time


def main():

    deletedFolders = 0
    deletedFiles = 0

    path = input("Enter Your Path: ")

    days = 30

    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):

        for main_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(main_folder):
                remove_folder(main_folder)
                deletedFolders += 1
                break

            else:
                for folder in folders:
                    folder_path = os.path.join(main_folder, folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deletedFolders += 1

                for file in files:
                    file_path = os.path.join(main_folder, file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deletedFiles += 1

        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(path)
                deletedFiles += 1

    else:
        print(f'"{path}" is not found')
        deletedFiles += 1

    print(f"Total folders deleted: {deletedFolders}")
    print(f"Total files deleted: {deletedFiles}")


def remove_folder(path):
    if not shutil.rmtree(path):
        print(f"{path} is removed successfully")

    else:
        print(f"Unable to delete the "+path)


def remove_file(path):

    if not os.remove(path):

        print(f"{path} is removed successfully")

    else:

        print("Unable to delete the "+path)


def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime

    return ctime


if __name__ == '__main__':
    main()
