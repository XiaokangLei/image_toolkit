'''
Descripttion: imgaug
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2022-11-25 12:51:07
LastEditors: Xiaokang Lei
LastEditTime: 2022-11-25 13:28:04
'''

import cv2
import imgaug.augmenters as iaa


def motion_blur(img, k=3, angle=0, direction=0.0):
    aug = iaa.MotionBlur(k=k, angle=angle, direction=direction)
    img_aug = aug.augment_image(img)
    return img_aug


if __name__ == '__main__':
    img = cv2.imread('../output/word/000000.jpg')
    new_img = motion_blur(img)
    print(type(img))
    cv2.imwrite("11.jpg", new_img)
