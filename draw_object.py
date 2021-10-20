# -*- coding: utf-8 -*-
# @Time    : 2021/3/5 0005 17:31
# @Author  : YJW
# @FileName: process_model.py
# @Software: PyCharm
import os
import cv2
import numpy as np
print(cv2.__file__)
def draw_object(jpg_path):
    print(jpg_path)
    print(type(jpg_path))
    font = cv2.FONT_HERSHEY_SIMPLEX
    status=os.system("cd ./ && ls")
    # status = os.chdir("../")
    image = cv2.imread("./Core_algorithm_of_rare_bird_object_detection/"+jpg_path)
    GrayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    x, y, w, h =cv2.boundingRect(GrayImage)
    print("-------------")
    print(x,y,w,h)

    if os.path.exists("./Core_algorithm_of_rare_bird_object_detection/" + jpg_path.split(".")[0] + ".txt"):
        print("0k")
    else:
        with open("Core_algorithm_of_rare_bird_object_detection/"+jpg_path.split(".")[0]+".txt","w") as f:
            f.write("Class:None, Box: 0 0 0 0")

    with open("Core_algorithm_of_rare_bird_object_detection/"+jpg_path.split(".")[0]+".txt","r") as f:
        pic_data=f.read().split("\n")
        print(pic_data)
        pic_data_item_i=0
        for pic_data_item_i in range(len(pic_data)-1):
            object_class = pic_data[pic_data_item_i].split(",")[0].split(":")[1]
            x1 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[1]
            x2 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[2]
            y1 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[3]
            y2 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[4]
            print(len(pic_data) - 1, pic_data_item_i)
            pic_data_item_i += 1
            if(h>=5000):
                draw = cv2.putText(image, object_class, (int(x1), int(y1) - 1), font, 2, (0, 255, 0), 7)
                draw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 7)
            elif(h>=4000):
                draw = cv2.putText(image, object_class, (int(x1), int(y1) - 1), font, 1.9, (0, 255, 0), 6)
                draw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 6)
            elif(h>=3000):
                draw = cv2.putText(image, object_class, (int(x1), int(y1) - 1), font, 1.5, (0, 255, 0), 5)
                draw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 5)
            elif(h>=2000):
                draw = cv2.putText(image, object_class, (int(x1), int(y1) - 1), font, 1.2, (0, 255, 0), 4)
                draw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            elif(h>=1000):
                draw = cv2.putText(image, object_class, (int(x1), int(y1) - 1), font, 1, (0, 255, 0), 3)
                draw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 3)
            elif(h>=500):
                draw = cv2.putText(image, object_class, (int(x1), int(y1) - 1), font, 0.8, (0, 255, 0), 2)
                draw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            else:
                draw = cv2.putText(image, object_class, (int(x1), int(y1) - 1), font, 0.5, (0, 255, 0), 1)
                draw = cv2.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 1)
    cv2.imwrite("./Core_algorithm_of_rare_bird_object_detection/"+jpg_path.split(".")[0]+"_out.jpg", draw)
    cv2.waitKey(0)
    cv2.destroyWindow("draw")

    return jpg_path.split(".")[0]+"_out.jpg"


if __name__ == '__main__':
    draw_object("data/haiou277.jpg")

