<template>
<div id="Content">
<div class="upload_predict">

  <div class="upload">
      <div id="upload_jpg">
          <img src="../assets/icon/upload_icon.jpg" alt="" class="upload_jpg_icon">
          <div id="true_upload_div">
            <input id="true_upload_jpg_input" type="file" ref="photo" @change="true_upload_jpg_input_function($event)" />
          </div>

          <img src="" alt="" ref="upload_jpg_preview_ref" id="upload_jpg_preview" v-show="upload_jpg_preview_show" accept="jpg" @click="handle_open_check_orginal_jpg">        
      </div>
      <div id="upload_text">
        <p>原始图像</p>
      </div>
     
  </div>
  <div id="classcount" v-show="classcount_show"> 
      <el-card shadow="always">
        衡水湖鸟类数量统计
      </el-card>

        {{classcount}}

  </div>
  <div class="predict">
    <div class="predict_result">
      <img src="" alt="" id="predict_result_img" ref="predict_result_img_ref" @click="handle_open_check_generate_jpg">
    </div> 
    <div id="predict_text">
        <p>检测结果</p>
      </div> 
  </div>
</div>
<div id="upload_check_orginal_jpg_preview_div" v-show="upload_check_orginal_jpg_preview_show"><img src="../assets/icon/upload_icon.jpg"  alt="" ref="upload_check_orginal_jpg_preview_ref" id="upload_check_orginal_jpg_preview"  @click="handle_close_check_orginal_jpg"></div>
<div class="result_text" >
  <div class="reupload">
    <div class="reupload_key" v-show="reupload_key_show" @click="windows_refresh"><svg t="1615364861264" class="reupload_key_icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1500" width="40px" height="40px"><path d="M585.25 847.05c-19.24 0-40.28-0.07-63.34-0.21-120.42-0.77-238.18-3.41-239.35-3.43a20.4 20.4 0 0 1-2.06-0.16c-2.07-0.26-51.31-6.73-101.4-34.54-68.46-38-105.37-97.26-106.73-171.31-0.94-51.26 7.62-95.59 25.44-131.78 14.66-29.77 35.48-54 61.89-72a194.78 194.78 0 0 1 76-30.56c5.06-22.53 17.39-66.86 43.08-110.41 49-83.09 122.5-122.72 212.5-114.63h0.47c61.55 7 109.12 24.72 145.43 54.12 29.46 23.85 52 54.92 72.21 99.69a274.51 274.51 0 0 1 87.26 15.91C846.52 365.78 912 407.69 940.57 505c29.15 99.29-4.55 179.92-38 230.08-35.68 53.59-84.52 92-107.8 102.24-7.42 3.27-22.2 9.73-209.52 9.73z m-300.61-43.61c12.5 0.28 121.4 2.62 233.64 3.37 217.91 1.46 254.66-4.34 260.77-6.26 12.5-5.65 56-36.22 90.27-87.64C898 669.84 927 600.76 902.19 516.27 883 451.06 843 407 783 385.38 737.75 369 698.38 372 698 372.05a20 20 0 0 1-20.09-12.22c-32.56-77.93-75.78-128.88-190.46-142C413 211.18 354.36 243.2 313.21 313c-31.92 54.11-40.88 110.66-41 111.23a20 20 0 0 1-19 16.95c-0.37 0-37.14 1.8-72.41 26.51-46.87 32.83-69.9 89.7-68.44 169 1.1 59.45 29.75 105.39 85.16 136.52 39.97 22.43 80.6 29.25 87.12 30.23z m-32.16-382.29z" p-id="1501" fill="#ffffff"></path><path d="M512.25 700.91a20 20 0 0 1-20-20V360.64a20 20 0 0 1 40 0v320.27a20 20 0 0 1-20 20z" p-id="1502" fill="#ffffff"></path><path d="M709.75 555.59a20 20 0 0 1-14-5.71L513.14 371l-185 178.5a20 20 0 1 1-27.78-28.78l213-205.5L723.75 521.3a20 20 0 0 1-14 34.29z" p-id="1503" fill="#ffffff"></path></svg> <div class="reupload_key_span">重新选择图像</div>  </div>
  </div>
  <div class="object_class">
    <el-table
    :data="tableData"
    border
    style="width: 100%">
    <el-table-column
      fixed
      prop="order"
      label="序号"
      width="60">
    </el-table-column>
    <el-table-column
      prop="Class"
      label="类别"
      width="80">
    </el-table-column>
    <el-table-column
      prop="x1"
      label="位置x1"
      width="70">
    </el-table-column>
    <el-table-column
      prop="y1"
      label="位置y1"
      width="70">
    </el-table-column>
    <el-table-column
      prop="x2"
      label="位置x2"
      width="70">
    </el-table-column>
    <el-table-column
      prop="y2"
      label="位置y2"
      width="70">
    </el-table-column>
    <el-table-column
      label="操作"
      width="60">
      <template slot-scope="scope">
        <el-button @click="handleCheckClick(scope.$index,scope.row)" type="text" size="small">查看</el-button>
      </template>
    </el-table-column>
    <el-table-column
      label="baidu"
      width="80">
      <template slot-scope="scope">
        <el-button @click="handleBaiduClick(scope.$index,scope.row)" type="text" size="small">baidubaike</el-button>
      </template>
    </el-table-column>
    <!-- <el-table-column
      prop="baidu"
      label="百度百科"
      width="100">
      <a href=""></a>
    </el-table-column> -->
    <el-table-column
      prop="level"
      label="保护级别"
      width="500">
    </el-table-column>
    <el-table-column
      prop="introduce"
      label="物种简介"
      width="500">
    </el-table-column>

  </el-table>
  </div>


</div>
</div>
</template>

<script>

import http from '@/utils/http';
export default {
  name: "Content",
  data() {
    return {
      upload_jpg_preview_show:false,
      reupload_key_show:false,
      orginal_jpg:"",
      generate_jpg:"",
      upload_check_orginal_jpg_preview_show:false,
      tableData: [],
      classcount:[],
      classcount_show:false
    }
  },
  methods: {
    handleBaiduClick(index,row){
      console.log(index,row)
      window.open(row["baidu"],'_blank')
    },
    handle_open_check_orginal_jpg(){
      this.upload_check_orginal_jpg_preview_show=true
      this.$refs.upload_check_orginal_jpg_preview_ref.src=this.orginal_jpg
    },
    handle_open_check_generate_jpg(){
      this.upload_check_orginal_jpg_preview_show=true
      this.$refs.upload_check_orginal_jpg_preview_ref.src=this.generate_jpg
    },
    handle_close_check_orginal_jpg(){
      this.upload_check_orginal_jpg_preview_show=false
    },
    windows_refresh(){
      window.location.reload();
    },
    base64ImgtoFile(dataurl, filename = 'file') {
      let arr = dataurl.split(',')
      let mime = arr[0].match(/:(.*?);/)[1]
      let suffix = mime.split('/')[1]
      let bstr = atob(arr[1])
      let n = bstr.length
      let u8arr = new Uint8Array(n)
      while (n--) {
        u8arr[n] = bstr.charCodeAt(n)
      }
      return new File([u8arr], `${filename}.${suffix}`, {
        type: mime
      })
    },
    true_upload_jpg_input_function(e_papa){
      var reader = new FileReader();
      reader.readAsDataURL(e_papa.path[0].files[0]);
      this.upload_jpg_preview_show=true
      let true_this=this
      reader.onload=function (e) {
        // console.log(e)
        var file=e_papa.target.files[0]
        // console.log(file)
        true_this.orginal_jpg=e.target.result
        document.getElementById('upload_jpg_preview').src=true_this.orginal_jpg
        let param = new FormData(); //创建form对象
        param.append("file", file)
        console.log(window.location.origin)
        let config = {headers: { "Content-Type": "multipart/form-data" }};
        http.post("upload",param,config).then((response) => {
          console.log(response)
          console.log(file.name)
          console.log(this)
          true_this.process_model(file.name)
        })
      }
    },
    process_model(test_jpg){
      console.log(test_jpg,"ok")
      let param={"test_jpg":test_jpg}
      console.log(typeof(param))
      http.post("process_model",param).then((response) => {
        console.log(response)
        this.draw_object(test_jpg)
      })
    },
    draw_object(test_jpg){
      let true_this=this
      let param={"test_jpg":test_jpg}
      http.post("draw_object",{params: param,responseType: 'arraybuffer'}).then((response) => {
        // console.log(response)

        // base64编码的图片
        console.log(response)
        var base64Img = 'data:image/jpg;base64,'+response;
        true_this.$refs.predict_result_img_ref.src=base64Img
        true_this.reupload_key_show=true
        true_this.generate_jpg=base64Img

        true_this.object_response(test_jpg)
      })
    },
    object_response(test_jpg){
      let param={"test_jpg":test_jpg}
      let true_this=this
      http.post("object_response",param).then((response) => {
        console.log(response)
        true_this.tableData=response[0]
        true_this.classcount=response[1]
        true_this.classcount_show=true
      })
    }
  },
}
</script>



<style scoped>
div{
  border: 0px;
  box-shadow:2px 2px 3px #000;
  background-color:rgb(246,246,246)
}
#Content {
  width: 85%;
  height: 100%;
  margin: 0 auto;
  background-color: rgb(246,246,246);
}
#upload_check_orginal_jpg_preview_div{
  width: 80%;
  height: 10%;
  /* background-color: chocolate; */
  position: relative;
  top: -400px;
  z-index:5555;
  /* height: 800px; */
  margin: 0 auto;
}
#upload_check_orginal_jpg_preview{
  width: 100%;
  height: 100%;
  margin: 0 auto;
}
.upload_predict {
  width: 100%;
  height: 400px;

  left: 0px;
  top: 0px;
}
.result_text {
  width: 100%;
  height: 400px;

  left: 0px;
  top: 50%;
}
.upload {
  width: 50%;
  height: 400px;
  
  left: 0;
  top: 0;
  position: relative;
}
.predict {
  width:50%;
  height: 400px;

  left: 50%;
  top: -100%;
  position: relative;
}
.object_class {
  width: 100%;
  height: 300px;
  /* background-color: darkkhaki; */
  left: 0;
  top: 0;
  position: relative;
}

#upload_jpg{
  width: 350px;
  height: 350px;
  margin: 0 auto;
  position: relative;
  /* background-color: blue; */
  border-radius: 5px;
  top: 0%;
}
.upload_jpg_icon{
  width: 100px;
  height: 100px;
  left: 35%;
  top: 35%;

  border-radius: 5px;
  position: relative;

}
#upload_text {
  width: 400px;
  height: 40px;
  margin: auto;
  background-color: rgb(33,179,185);
  text-align: center;
  line-height: 40px;
  border-radius: 5px;
  position: relative;
  top: -10px;
}
.predict_result{
  width: 350px;
  height: 350px;
  margin: 0 auto;
  position: relative;
  border-radius: 5px;
  top: 0%;

}
#predict_result_img {
  width: 350px;
  height: 350px;
}
#predict_text {
  width: 400px;
  height: 40px;
  margin: auto;
  background-color: rgb(33,179,185);
  text-align: center;
  line-height: 40px;
  border-radius: 5px;
  position: relative;
  top: -10px;
}
.reupload{
  width: 100%;
  height: 100px;

  left: 0;
  top: 0;
  position: relative;
}
.reupload_key{
  width: 300px;
  font-size: 20px;
  height: 50px;
  overflow:hidden;
  top: 20px;
  left: 15%;
  position: relative;
  background-color: rgb(33,179,185);
  border-radius: 5px;
  
}
.reupload_key_icon{
  position: relative;
  top: 5px;
  left:10%;
}
.reupload_key_span{
  position:relative;
  top:-33px;
  background-color: rgb(33,179,185);
  left:30%;
  box-shadow:0 0 0 #000;
}
#true_upload_div{
  /* background-color: blue; */
  width: 100px;
  height: 100px;
  position: relative;
  left: 35%;
  top: 0%;
  overflow: hidden;
  opacity:0;

}
#true_upload_jpg_input{
  width: 100px;
  height: 100px;
  opacity:0
}
#upload_jpg_preview{
  width: 350px;
  height: 350px;
  position: relative;
  top: -58%;
}
#upload_check_orginal_jpg_preview{
  width: 1080x;
  margin: 0 auto;
  height: 500px;
  /* background-color: chartreuse; */
}
#classcount{
  width: 200px;
  height: 200px;
  background-color: white;
  z-index:5555;
  position:fixed;
  border-radius: 2px;
  top: 30%;
  left: 44%;
  box-shadow:0px 0px 0px #000;
  text-align: center;
}
</style>


