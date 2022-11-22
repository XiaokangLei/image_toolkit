'''
Descripttion: tools
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-22 12:27:38
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-22 12:36:25
'''

import os


def get_file_list(dir, filelist=[], ext=None):
    """get files from dir

    Args:
        dir (str): files of dir
        ext (_type_, optional): _description_. Defaults to None.

    Returns:
        list: file name list
    """
    newdir = dir
    # file
    if os.path.isfile(dir):
        if ext is None:
            filelist.append(dir)
        elif ext in dir[-3:]:
            filelist.append(dir)
    # dir
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            newdir = os.path.join(dir, s)
            get_file_list(newdir, filelist, ext)

    return filelist
