'''
Descripttion: Extract images from word file
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-22 11:44:35
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-23 11:29:04
'''

import zipfile
import os
import shutil


def word2img(word_path, result_path):
    """Extract images from word file

    Args:
        word_path (str): path of word file
        result_path (str): path of asving images

    Returns:
        str: path of every image or None if no image
    """
    tmp_path = f'{os.path.splitext(word_path)[0]}'
    # 拷贝源文件后重命名再解压
    splitext = os.path.splitext(word_path)
    zip_path = shutil.copy(word_path, f'{splitext[0]}_new{splitext[1]}')
    with zipfile.ZipFile(zip_path, 'r') as f:
        for file in f.namelist():
            f.extract(file, tmp_path)
    os.remove(zip_path)
    # 注：word图片在zip文件内的word/media目录下
    pic_path = os.path.join(tmp_path, 'word/media')
    if not os.path.exists(pic_path):
        shutil.rmtree(tmp_path)
        return 'no pictures found'
    pictures = os.listdir(pic_path)
    if not os.path.exists(result_path):
        os.makedirs(result_path)
    for picture in pictures:
        # 根据word的文件名生成图片的名称
        word_name = os.path.splitext(word_path)[0]
        if os.sep in word_name:
            new_name = word_name.split('\\')[-1]
        else:
            new_name = word_name.split('/')[-1]
        picture_name = f'{new_name}_{picture}'
        shutil.copy(os.path.join(pic_path, picture), os.path.join(result_path, picture_name))

    shutil.rmtree(tmp_path)
    return (os.path.join(result_path, pic) for pic in os.listdir(result_path))


def word2img2(word_path, result_path):
    """Extract images from word file

    Args:
        word_path (str): path of word file
        result_path (str): path of asving images

    Returns:
        str: path of every image or None if no image
    """
    import docx
    import re
    doc = docx.Document(word_path)
    dict_rel = doc.part._rels
    for rel in dict_rel:
        rel = dict_rel[rel]
        if "image" in rel.target_ref:
            if not os.path.exists(result_path):
                os.makedirs(result_path)
            img_name = re.findall("/(.*)", rel.target_ref)[0]
            word_name = os.path.splitext(word_path)[0]
            if os.sep in word_name:
                new_name = word_name.split('\\')[-1]
            else:
                new_name = word_name.split('/')[-1]
            img_name = f'{new_name}_{img_name}'
            with open(f'{result_path}/{img_name}', "wb") as f:
                f.write(rel.target_part.blob)


if __name__ == '__main__':
    # path of word file
    docx_path = r'../images/word/02.22.docx'
    # path of asving images
    result_path = r'../output/word'
    m = word2img(docx_path, result_path)
