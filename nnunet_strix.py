import json
import os

def get_nnunet_case_files(nnUNet , dataset = None):
    with open(nnUNet) as json_file:
        nnUNet_data = json.load(json_file)

    training_list = nnUNet_data["training"]

    num = len(nnUNet_data["training"])
    dataset = []
    i = 0
    for i in range(num):
        case_data = {}
        image_relpath = training_list[i]["image"]
        label_relpath = training_list[i]["label"]
        #mask_relpath = training_list[i]["mask"]#此处应加判断
        case_data['image'] = os.path.abspath(image_relpath)
        case_data['label'] = os.path.abspath(label_relpath)#?
        #case_data['mask'] = os.path.abspath(mask_relpath)
        dataset.append(case_data)
        i = i + 1
    print(dataset)

nnUNet = r'C:\Users\Qi Zhang\Documents\WeChat Files\wxid_fj1t1hokcu8h12\FileStorage\MsgAttach\48349edd9a01ff35af8f80b8a71854d9\File\2022-09\dataset.json'
get_nnunet_case_files(nnUNet)