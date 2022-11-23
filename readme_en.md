<!--
 * @Descripttion: Image Processing
 * @version: V1.0
 * @Author: Xiaokang Lei
 * @email: lxk201808@163.com
 * @Date: 2022-11-23 11:44:24
 * @LastEditors: Xiaokang Lei
 * @LastEditTime: 2022-11-23 11:52:00
-->

# Image Processing

This project mainly uses Python to implement common methods in image processing, including image enhancement, affine transformation, image blur, PDF/Word image extraction, etc. Long-term updates, welcome to star~

## Contents

- images：Store test image/file path
- output：Store image processing result file path
- utils：Main image processing code storage path, each processing a file
- img_test.py：Test code, call functions in utils
- requirements.txt：The environment used by each method is divided by '#' (note that not every method uses all the environments in requirements)

## Methods

- utils/word_extract_img.py：Extract all pictures in Word, support '.docx'
- utils/hexdigest.py：Calculate the file checksum, including 'md5', 'sha1', 'sha256' three algorithms
- utils/remove_same_file.py：Remove duplicate files based on file verification code
