'''
Descripttion: find/remove the same files
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-23 10:14:08
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-23 11:43:07
'''

import os
from .util import get_file_list
from .hexdigest import encrypt


def find_by_md5(file_dir: str, algorithm: str) -> None:
    """ find the same files

    Args:
        file_dir (str): files dir
        algorithm (str): hexdigest algorithm
    """
    file_names = get_file_list(file_dir)
    file_dict = {}

    for file_path in file_names:
        hexdigest = encrypt(file_path, algorithm)
        key = '{}'.format(hexdigest)
        if key in file_dict:
            file_dict[key].append(file_path)
        else:
            file_dict[key] = [file_path]

    print("==> The Same Files: ")
    for _, files in file_dict.items():
        if len(files) > 1:
            print(files)


def find_and_remove_repeat(file_dir: str, algorithm: str) -> None:
    """ find the same files and delete the same files

    Args:
        file_dir (str): files dir
        algorithm (str): hexdigest algorithm
    """
    file_names = get_file_list(file_dir)
    file_dict = {}

    for file_path in file_names:
        hexdigest = encrypt(file_path, algorithm)
        key = '{}'.format(hexdigest)
        if key in file_dict:
            file_dict[key].append(file_path)
        else:
            file_dict[key] = [file_path]

    print("==> The Same Files: ")
    for _, files in file_dict.items():
        if len(files) > 1:
            print("=> Keep: \n" + files[0])
            print("=> Remove: ")
            for file in files[1:]:
                print(file)
                os.remove(file)


if __name__ == '__main__':
    img_dir = '../output/word'
    # 'md5', 'sha1', 'sha256'
    algorithm = 'md5'
    # Find the same file
    find_by_md5(img_dir, algorithm)
    # Find the same file and delete the same file
    # find_and_remove_repeat(img_dir, algorithm)
