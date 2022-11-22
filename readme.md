<!--
 * @Descripttion: Python 图像处理常用方法
 * @version: V1.0
 * @Author: Xiaokang Lei
 * @email: lxk201808@163.com
 * @Date: 2022-11-22 12:13:11
 * @LastEditors: Xiaokang Lei
 * @LastEditTime: 2022-11-22 12:25:22
-->

# Python 图像处理常用方法

本项目主要使用Python实现图像处理中常用的方法，包括图像增强、仿射变换、图像模糊、PDF/Word提取图片等，长期更新，欢迎star~

## 目录说明

- images：存放测试图片/文件路径
- output：存放图片处理结果文件路径
- utils：主要图像处理代码存放路径，每种处理一个文件
- img_test.py：测试代码，调用utils中的函数
- requirements.txt：每个方法使用到的环境，按#分割（注意，不是每个方法都用到requirements中的所有环境）

## 图像处理方法

- utils/word_extract_img.py：提取Word中的所有图片，支持.docx
