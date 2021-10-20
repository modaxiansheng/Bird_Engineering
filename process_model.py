# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 0005 17:31
# @Author  : YJW
# @FileName: process_model.py
# @Software: PyCharm
import os
import numpy as np
def process_model(jpg_path):
    if os.path.exists("./Core_algorithm_of_rare_bird_object_detection/"+jpg_path.split(".")[0]+".txt"):
        print("0k")
        os.remove("./Core_algorithm_of_rare_bird_object_detection/"+jpg_path.split(".")[0]+".txt")
        os.remove("./Core_algorithm_of_rare_bird_object_detection/" + jpg_path + ".png")
    # status=os.system("cd .. && ls")
    status = os.system("cd ./ && ls")
    status=os.chdir("./Core_algorithm_of_rare_bird_object_detection")

    status = os.system("darknet detector test voc_bird.data yolov4_baidubird_20201026.cfg yolov4_baidubird_20201026_final.weights "+jpg_path+" -thresh=0.25")

    status = os.chdir("../")
    status= os.system("cd ./ && ls")
    print(status)
    return status
if __name__ == '__main__':
    process_model("data/haiou277.jpg")