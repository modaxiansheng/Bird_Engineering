<template>
<div id="Work">
  <div>
    <img ref="test" src="" alt="">
    <div v-for="(single_object,i) in history_list" class="history_list">
      <div v-for="(single_object_item,i) in single_object" class="single_object">
        <div class="single_object_count">
          <h4>鸟类数量信息</h4>
          <h5>{{single_object_item[2]}}</h5>
        </div>
        <div class="single_object_original">
          <img :src="single_object_item[3]" alt="" class="single_object_original_jpg" ref="single_object_original_ref">
        </div>
        <div class="single_object_out">
          <img :src="single_object_item[4]"  alt="" class="single_object_out_jpg" ref="single_object_out_ref">
        </div>
        <!-- <div class="button_desc"><button @click="handle_check_object_desc">查看目标鸟类详细信息</button></div> -->
        <div class="object_desc">
          <el-table
            :data="single_object_item[1]"
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
  </div>
</div>
</template>

<script>

import http from '@/utils/http';
export default {
  name: "Work",
  data() {
    return {
      history_list:[]
    }
  },
  mounted(){
    let true_this=this
    http.get("/data_response").then((response) => {
      // console.log(response)
      true_this.history_list=response
      // console.log(true_this.history_list)
      // console.log(true_this.history_list[0][0][3].replace("b'","").replace("'",""))
      // true_this.$refs.test.src= true_this.history_list[0][0][3]
    })
  }
}
</script>



<style scoped>
div{
  border: 0px;
  /* box-shadow:2px 2px 3px #000; */
  background-color:rgb(246,246,246)
}
#Work {
  width: 85%;
  height: 100%;
  margin: 0 auto;
  background-color: rgb(246,246,246);
}
.button_desc{
  width: 100px;
  height: 100px;
  background-color: salmon;
}
.history_list{
  border: 1px solid #000;
  padding-bottom: -500px;
}
.single_object_count{
  text-align: center;
}
.single_object{
  border: 5px solid rgb(84,92,100)
}
.single_object_item1_child{
  border: 1px solid green;
}
.single_object_original{
  position: relative;
  width: 40%;
  left: 20%;
  
}
.single_object_out{
  width: 40%;
  position: relative;

  left: 50%;
  top: -205px;
}
.single_object_original_jpg,.single_object_out_jpg{
  height: 200px;
}
.object_desc{
  position: relative;
  top: -200px;
}
</style>


