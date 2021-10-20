import time
from flask import *
import cv2
import base64
import os
import process_model as process_model
import draw_object as draw_object
from collections import Counter
from turbojpeg import TurboJPEG
from history_search import *
app = Flask(__name__, template_folder="./dist", static_folder="./dist", static_url_path="")

# process_model.process_model("data/haiou277.jpg")
# draw_object.draw_object("data/haiou277.jpg")
def load_turbojpeg():
    basePath = os.path.split(os.path.realpath(__file__))[0]
    print(basePath)
    TurboJPEGPath = basePath + '\\turbojpeg.dll'
    turbojpeg = TurboJPEG(TurboJPEGPath)
    return turbojpeg

turbojpeg = load_turbojpeg()

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    file = request.files['file']
    print(type(file))
    print(str(time.time()).split(".")[0], file.filename)
    if file and file.filename.split(".")[1]=="jpg":
        file.save("./Core_algorithm_of_rare_bird_object_detection/data/"+file.filename)
    #     process_model.process_model("data/haiou277.jpg")
        return jsonify({'status': "upload_sucess"+file.filename})
    return jsonify({'status': 0})

@app.route('/process_model', methods=['POST'])
def process():
    # 说明：jupyter 可以调用这个
    # json = str(request.data).split("'")[1]
    # 说明：前端ajax 可以调用这个
    json=request.get_json()["test_jpg"]
    status=process_model.process_model("data/"+json)
    if status==0:
        return jsonify({'status': "process_model_sucess"+json})
    return jsonify({'status': 0})

@app.route('/draw_object', methods=['POST'])
def draw():
    # 说明：jupyter 可以调用这个
    # json = str(request.data).split("'")[1]
    # 说明：前端ajax 可以调用这个
    json=request.get_json()["params"]["test_jpg"]
    print(json)
    out_object=draw_object.draw_object("data/"+json)
    if out_object:
        # image = cv2.imread('./Core_algorithm_of_rare_bird_object_detection/'+out_object)
        # jpeg = turbojpeg.encode(image)
        # resp = make_response(jpeg)
        # return resp
        path = './Core_algorithm_of_rare_bird_object_detection/'+out_object
        f = open(path, 'rb')
        base64_str = base64.b64encode(f.read())
        print(type(base64_str))
        return base64_str
    return jsonify({'status': 0})

@app.route('/object_response', methods=['POST'])
def object_response_result():
    # 说明：jupyter 可以调用这个
    # json = str(request.data).split("'")[1]
    # 说明：前端ajax 可以调用这个
    json=request.get_json()["test_jpg"]
    class_array = []
    print(json)
    with open('./Core_algorithm_of_rare_bird_object_detection/data/'+json.split(".")[0]+".txt","r") as f:
        pic_data = f.read().split("\n")
        print(pic_data)
        pic_data_item_i = 0
        pic_data_json=[]
        for pic_data_item_i in range(len(pic_data) - 1):
            object_class = pic_data[pic_data_item_i].split(",")[0].split(":")[1]
            x1 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[1]
            x2 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[2]
            y1 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[3]
            y2 = pic_data[pic_data_item_i].split(",")[1].split(":")[1].split(" ")[4]
            print(len(pic_data) - 1, pic_data_item_i)

            pic_data_item_i += 1
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
            class_index = list.index(object_class)
            with open("level.txt", "r") as f_level:
                level_data = f_level.read().split("#\n")
                print(class_index)
                print(level_data[class_index].split(";")[0].split(":")[1])
                class_array.append(level_data[class_index].split(";")[1].split(":")[1])
                pic_data_json.append({"order":pic_data_item_i,"Class":level_data[class_index].split(";")[1].split(":")[1],"x1":x1,"x2":x2,"y1":y1,"y2":y2,"baidu":level_data[class_index].split(";")[2].split("$")[1],"level":level_data[class_index].split(";")[3].split(":")[1],"introduce":level_data[class_index].split(";")[4].split(":")[1]})
        return jsonify(pic_data_json,Counter(class_array))
    return jsonify({'status': 0})



@app.route('/data_response', methods=['GET'])
def return_data_response():
    os.system("python history_search.py")
    all_txt_object_detail = get_txt_object_detail(txt_function(all_result))
    # print(all_txt_object_detail)
    return jsonify(all_txt_object_detail)

# @app.route('/data_original_response', methods=['GET'])
# def get_original_object_detail():
#     all_txt_file=txt_function(all_result)
#     result=[]
#     for txt_file in all_txt_file:
#         f_original_jpg = open(txt_file.split("txt")[0] + "jpg", 'rb')
#         base64_original_jpg = base64.b64encode(f_original_jpg.read())
#         result.append(str(base64_original_jpg))
#         print(jsonify(result))
#     return jsonify(result)

if __name__ == '__main__':
    # http_server = WSGIServer(('0.0.0.0', 5000), app)
    # http_server.serve_forever()
    app.run(host='0.0.0.0', port=5000)