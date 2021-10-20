# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 0008 17:53
# @Author  : YJW
# @FileName: test.py
# @Software: PyCharm
from flask import *
import os
import time
import base64
from collections import Counter


dirname="./Core_algorithm_of_rare_bird_object_detection/data"

def data_return_response(dirname):
    result = []  # 所有的文件

    for maindir, subdir, file_name_list in os.walk(dirname):

        for filename in file_name_list:
            apath = os.path.join(maindir, filename)  # 合并成一个完整路径
            result.append(apath)

    return result

all_result=data_return_response(dirname)

def outcome_jpg_function(all_result):
    result=[]
    for outcome_jpg_item in all_result:
        if outcome_jpg_item.split("out.")[-1]=="jpg":
            result.append(outcome_jpg_item)
    return result

def original_jpg_function(all_result):
    result=[]
    for original_jpg_item in all_result:
        if original_jpg_item.split(".")[-1]=="jpg":
            if original_jpg_item.split("out.")[-1]!="jpg":
                result.append(original_jpg_item)
    return result

def txt_function(all_result):
    result=[]
    for txt_item in all_result:
        if txt_item.split(".")[-1]=="txt":
            result.append(txt_item)
    return result

# print(original_jpg_function(all_result))
#
# print(outcome_jpg_function(all_result))
#
# print(txt_function(all_result))

def get_txt_file_create_detail(all_txt_file):
    result=[]
    for file_item in all_txt_file:
        file_create_time=time.ctime(os.stat(file_item).st_ctime)
        result.append({file_item,file_create_time})
    return result
print(get_txt_file_create_detail(txt_function(all_result)))

def get_txt_object_detail(all_txt_file):
    result=[]

    list = ["baiqueling0",
            "bailu1",
            "haiou2",
            "heizuiou3",
            "huiqiongniao4",
            "luzi5",
            "shanmaque6",
            "xiaopiti7",
            "zhuomuniao8",
            "dae9"]
    for txt_file in all_txt_file:
        singe_txt_file=[]
        class_array = []
        with open(txt_file,"r") as f:
            pic_data = f.read().split("\n")
            pic_data_item_i = 0
            pic_data_json=[]
            for pic_data_item_i in range(len(pic_data) - 1):
                object_class = pic_data[pic_data_item_i].split(",")[0].split(":")[1]
                x1 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[1]
                x2 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[2]
                y1 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[3]
                y2 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[4]
                # print(len(pic_data) - 1, pic_data_item_i)

                pic_data_item_i += 1

                class_index = list.index(object_class)
                with open("level.txt", "r") as f_level:
                    level_data = f_level.read().split("#\n")
                    # print(class_index)
                    # print(level_data[class_index].split(";")[0].split(":")[1])
                    class_array.append(level_data[class_index].split(";")[1].split(":")[1])
                    # single_object_count=Counter(class_array)

                    pic_data_json.append({"order":pic_data_item_i,"Class":level_data[class_index].split(";")[1].split(":")[1],"x1":x1,"x2":x2,"y1":y1,"y2":y2,"baidu":level_data[class_index].split(";")[2].split("$")[1],"level":level_data[class_index].split(";")[3].split(":")[1],"introduce":level_data[class_index].split(";")[4].split(":")[1]})
                f_original_jpg = open(txt_file.split("txt")[0]+"jpg", 'rb')
                base64_original_jpg = base64.b64encode(f_original_jpg.read())
                f_out_jpg = open(txt_file.split(".txt")[0]+"_out.jpg", 'rb')
                base64_out_jpg = base64.b64encode(f_out_jpg.read())

            object_values_cnt = {}
            for value in class_array:
                object_values_cnt[value] = object_values_cnt.get(value, 0) + 1
            print("================================================")
            print('data:image/jpg;base64,'+str(base64_original_jpg).replace("b'","").replace("'",""))
            base64_original_jpg_str='data:image/jpg;base64,'+str(base64_original_jpg).replace("b'","").replace("'","")
            base64_out_jpg_str='data:image/jpg;base64,'+str(base64_out_jpg).replace("b'","").replace("'","")
            print("================================================")
            singe_txt_file.append([txt_file,pic_data_json,object_values_cnt,base64_original_jpg_str,base64_out_jpg_str])
        result.append(singe_txt_file)
    return result





