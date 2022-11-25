'''
Descripttion: rename images
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-23 14:53:31
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-25 13:06:15
'''

import os
from PIL import Image


# Image extension supported.
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'JPG', 'PNG', 'bmp', 'jpeg', 'JPEG'])


def allowed_file(filename : str):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


def is_valid_image(img_path: str) -> bool:
    """Determine whether the file is a valid (complete) image

    Args:
        img_path (str): image path

    Returns:
        bool: valid or not
    """
    bvalid = True
    try:
        Image.open(img_path).verify()
    except:
        bvalid = False
    return bvalid


def transimg(img_path: str) -> bool:
    """Convert image format

    Args:
        img_path (str): image path

    Returns:
        bool: success or not
    """
    if is_valid_image(img_path):
        try:
            str_name = img_path.rsplit(".", 1)
            output_img_path = str_name[0] + ".jpg"
            print(output_img_path)
            im = Image.open(img_path)
            im.save(output_img_path)
            return True
        except:
            return False
    else:
        return False


def rename(img_path: str, index: int) -> None:
    """ rename image

    Args:
        img_path (str): image path
        index (int): name starts from index
    """
    filelist = os.listdir(img_path)
    total_num = len(filelist)
    count = 0
    for item in filelist:
        if allowed_file(item):
            filename_suffix = '.' + item.rsplit('.', 1)[1]
            src = os.path.join(os.path.abspath(img_path), item)
            dst = os.path.join(os.path.abspath(img_path), '00' + format(str(index), '0>4s') + filename_suffix)
            try:
                os.rename(src, dst)
                print('converting %s to %s' % (src, dst))
                index = index + 1
                count = count + 1
            except:
                index = index + 1
                continue
    print('total %d to rename & converted %d jpgs' % (total_num, count))


if __name__ == '__main__':
    img_dir = '../output/word'
    index = 0
    rename(img_dir, index)
