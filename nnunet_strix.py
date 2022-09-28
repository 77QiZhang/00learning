import json
import os
def get_nnunet_case_files(nnUNet , out_file_path,dataset = None):
    with open(nnUNet) as json_file:
        nnUNet_data = json.load(json_file)
    out_file = open(out_file_path,mode='w')
    training_list = nnUNet_data["training"]#是个列表

    num = len(nnUNet_data["training"])
    dataset = []
    i = 0
    
    for i in range(num):
        case_data = {}
        if "image" not in training_list[i]:
            pass
        else:
            image_relpath = training_list[i]["image"]
            case_data['image'] = os.path.abspath(image_relpath)
        if "label" not in training_list[i]:
            pass
        else:
            label_relpath = training_list[i]["label"]
            case_data['label'] = os.path.abspath(label_relpath)
        if "mask" not in training_list[i]:
            pass
        else:
            mask_relpath = training_list[i]["mask"]
            case_data['mask'] = os.path.abspath(mask_relpath)
        dataset.append(case_data)
        i = i + 1
        #相对路径转绝对路径os.path.abspath(path)
    print(dataset)
    json.dump(dataset,out_file,indent=4)


nnUNet = r'C:\Users\Qi Zhang\Documents\WeChat Files\wxid_fj1t1hokcu8h12\FileStorage\MsgAttach\48349edd9a01ff35af8f80b8a71854d9\File\2022-09\dataset.json'
out_file_path = r'D:\code\nnUNet_Strix_outfile.json'
get_nnunet_case_files(nnUNet,out_file_path)