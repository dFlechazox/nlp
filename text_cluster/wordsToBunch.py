#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@version: python3.6
@author: XiangguoSun
@contact: sunxiangguodut@qq.com
@file: corpus2Bunch.py
@time: 2018/1/23 16:12
@software: PyCharm
"""

import os
import pickle

from sklearn.datasets.base import Bunch
from filetools import readfile


def corpus2Bunch(wordbag_path, seg_path, class_num, sample_num):
    catelist = os.listdir(seg_path)  # 获取seg_path下的所有子目录，也就是分类信息
    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)
    '''
    extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充
    原来的list
    '''
    # 获取每个目录下所有的文件
    i = 0
    for mydir in catelist:
        if i == class_num:
            break
        i = i+1
        class_path = seg_path + mydir + "/"  # 拼出分类子目录的路径
        file_list = os.listdir(class_path)  # 获取class_path下的所有文件
        j=0
        for file_path in file_list:  # 遍历类别目录下文件
            if j == sample_num:  # 每类400
                break
            j=j+1
            fullname = class_path + file_path  # 拼出文件名全路径
            bunch.label.append(mydir)
            bunch.filenames.append(fullname)
            bunch.contents.append(readfile(fullname))  # 读取文件内容
            '''append(element)是python list中的函数，意思是向原来的list中添加element，注意与extend()函数的区别'''
    # 将bunch存储到wordbag_path路径中
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("构建文本对象结束！！！")


if __name__ == "__main__":
    # 对数据集进行Bunch化操作：
    wordbag_path = "word_bag/dataset.dat"  # Bunch存储路径
    seg_path = "dataset_res/"  # 分词后分类语料库路径
    corpus2Bunch(wordbag_path, seg_path, 12, 400)
