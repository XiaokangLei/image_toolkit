'''
Descripttion: Images Toolkit
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-22 11:43:33
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-23 15:23:34
'''

from utils.remove_same_file import find_by_md5, find_and_remove_repeat
from utils.rename_img import rename
from utils.word_extract_img import word2img
from utils.util import get_file_list


def word_extract_img_test():
    """Extract images from word file
    """
    path = r'./images/word/20221122.docx'
    store_path = r'./output/word'
    # One file
    res = word2img(path, store_path)
    # Multiple files
    # test_file_path = './images/word/'
    # test_file_list = get_file_list(test_file_path)
    # for file_path in test_file_list:
    #     img_path = test_file_path + file_path.split('/')[-1]
    #     res = word2img(img_path, store_path)


def remove_same_img_test():
    """Find/remove the same files
    """
    img_dir = './output/word'
    # 'md5', 'sha1', 'sha256'
    algorithm = 'md5'
    # Find the same file
    find_by_md5(img_dir, algorithm)
    # Find the same file and delete the same file
    # find_and_remove_repeat(img_dir, algorithm)


def rename_img():
    img_dir = './output/word'
    index = 0
    rename(img_dir, index)


if __name__ == '__main__':
    # Test Word Extract Images
    # word_extract_img_test()
    # Test Remove Same Images
    # remove_same_img_test()
    # Test Rename Images
    rename_img()
