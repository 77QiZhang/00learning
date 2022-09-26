#相对路径转绝对路径
from cProfile import label
from email.mime import image
import numpy as np
import os
import json
from pathlib import Path
from random import shuffle
import nibabel as nib

#先从nnunet的data.json中提取路径
#转绝对路径
#整合

def get_nnunet_case_files(nnUNet , dataset = None):
    nnUNet["training"]=json.loads(nnUNet["training"])#把json格式转为python识别的格式
    training_list = nnUNet["training"]#是个列表

    num = len(nnUNet["training"])
    dataset = []
    i = 0#存疑
#建立一个列表，列表的第几位是一个字典
    for i in num:
        case_data = {}
        image_relpath = training_list[i]["image"]
        label_relpath = training_list[i]["label"]
        mask_relpath = training_list[i]["mask"]
        case_data['image'] = os.path.abspath(image_relpath)
        case_data['label'] = os.path.abspath(label_relpath)
        case_data['mask'] = os.path.abspath(mask_relpath)
        dataset.append(case_data)
        i = i + 1
        #相对路径转绝对路径os.path.abspath(path)
    print(dataset)

nnUNet = r'C:\Users\37225\Documents\WeChat Files\wxid_fj1t1hokcu8h12\FileStorage\File\2022-09\dataset.json'
get_nnunet_case_files(nnUNet)