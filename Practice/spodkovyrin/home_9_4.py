import time
import os
import shutil


def remove_folder(path):
    # if not shutil.rmtree(path):
    deleted_folders_count = 0
    if len(os.listdir(path)) == 0:
        shutil.rmtree(path)
        print(f'{path} Успешно удален')
        deleted_folders_count += 1
        print(f'Папок удалено: {deleted_folders_count}')
    else:
        pass


def remove_file(path):
    # if not os.remove(path):
    deleted_files_count = 0
    if os.path.isfile(path):
        os.remove(path)
        print(f"{path} Успешно удален")
        deleted_files_count += 1
        print(f'Файлов удалено: {deleted_files_count}')
    else:
        pass


def get_age(path):
    ctime = os.stat(path).st_ctime
    return ctime


path = r'E:\Study\PythonCourseKupno\Practice\spodkovyrin\work_test'
time_folders = 2
time_files = 1


while True:
    seconds_folders = time.time() - (time_folders * 60)
    seconds_files = time.time() - (time_files * 60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            for folder in folders:
                folder_path = os.path.join(root_folder, folder)
                if seconds_folders >= get_age(folder_path):
                    remove_folder(folder_path)
                else:
                    for folder in folders:
                        folder_path = os.path.join(root_folder, folder)
                        if seconds_folders >= get_age(folder_path):
                            remove_folder(folder_path)
                    for file in files:
                        file_path = os.path.join(root_folder, file)
                        if seconds_files >= get_age(file_path):
                            remove_file(file_path)
            for file in files:
                file_path = os.path.join(root_folder, file)
                if seconds_files >= get_age(file_path):
                    remove_file(file_path)
        else:
            if seconds_files >= get_age(path):
                remove_file(path)
    else:
        print(f'"{path}" is not found')
