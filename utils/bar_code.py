'''
Descripttion: Bar code identification
version: V1.0
Author: Xiaokang Lei
email: lxk201808@163.com
Date: 2023-01-16 16:36:10
LastEditors: Xiaokang Lei
LastEditTime: 2023-01-29 11:55:38
'''

import cv2
import pyzbar.pyzbar as pbar

# pip install opencv-python
# pip install pyzbar

if __name__ == '__main__':

    img_path = r'../images/barcode/test07.jpg'

    image = cv2.imread(img_path)
    barcodes = pbar.decode(image)
    print(barcodes)

    barcode = barcodes[0]
    barcode_data = barcode.data.decode('utf-8')

    print(barcode_data)
