import os
import shutil


def get_file_name_extension(filename):
    """
    Get the name and extension of the filename.

    :param filename: The filename to split

    :return: `name` and `ext`
    """
    splits = os.path.splitext(filename)
    name, ext = splits[0], splits[1]
    return name, ext


def get_file_content(filename):
    """
    Read content from file.
    :param filename:
    :return:
    """
    if not filename:
        return None
    with open(filename, mode='r') as file:
        content = file.read()
    return content


def directory_listing(folder_name, file_type=None):
    """
    Listing all file in specific directory.

    :param folder_name: The folder from which files are loaded.

    :param file_type: The specific kind of files to load.

    :return:
    """
    if not folder_name or str(folder_name).__eq__(''):
        raise Exception("Folder must not be empty.")
    files = []
    allfiles = os.listdir(folder_name)
    for x in allfiles:
        # if os.path.isfile(folder_name+"/"+x):  # we need only file to return
        if not file_type:
            files.append(x)
        else:
            if str(x).endswith(file_type):
                files.append(x)
    return files


def file_info_gathering(filename):
    if not filename:
        raise Exception("The file name can not be empty")
    if not os.path.isfile(filename):
        raise Exception("The file" + filename + "does not exist or corrupt. Please check again.")
    info = os.stat(filename)
    return info


def copy_file(source_file, target_file):
    if not source_file:
        raise Exception("Check the input filename please. It can not be empty")
    if not os.path.isfile(source_file):
        raise Exception("File does not exist.")
    shutil.copy2(source_file, target_file)


def rename_directory(source_dir, target_dir):
    if not source_dir:
        raise Exception("Check the source directory name. It can not be empty.")
    if not target_dir:
        raise Exception("Check the destination directory name. It can not be empty.")
    shutil.move(source_dir, target_dir)


def create_dir(directory):
    if not os.path.exists(directory):
        try:
            os.makedirs(directory)
            return True
        except Exception as e:
            print(e.__str__())
            return False


def move_file_to_directory(source_file, target_dir):
    if not source_file:
        raise Exception("Check the source file name. It can not be empty.")
    if not target_dir:
        raise Exception("Check the destination directory name. It can not be empty.")
    shutil.move(source_file, target_dir)
