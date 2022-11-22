'''
Descripttion: Images Toolkit
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-22 11:43:33
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-22 12:40:03
'''

from utils.word_extract_img import word2img
from utils.util import get_file_list

if __name__ == '__main__':
    # 源文件
    path = r'./images/word/20221122.docx'
    # 最后保存结果的文件夹
    store_path = r'./output/word'

    # 单个文件处理
    res = word2img(path, store_path)

    # 批量处理
    # test_file_path = './images/word/'

    # test_file_list = get_file_list(test_file_path)
    # for file_path in test_file_list:
    #     img_path = test_file_path + file_path.split('/')[-1]
    #     res = word2img(path, store_path)
