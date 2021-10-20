<template>
<div id="Header">
  <el-menu
    :default-active="activeIndex2"
    class="el-menu-demo"
    mode="horizontal"
    @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">
    <el-menu-item index="1" @click="handle_home_Click">首页</el-menu-item>
    <el-menu-item index="2" @click="handle_work_Click">我的工作台</el-menu-item>
  </el-menu>
</div>
</template>
<script>
export default {
  name: "Header",
  data() {
    return {
      activeIndex: '1',
      activeIndex2: '1'
    };
  },
  methods: {
    handleSelect(key, keyPath) {
      console.log(key, keyPath);
    },
    handle_home_Click(){
      this.$router.push({path:'content'}) 
    },
    handle_work_Click(){
      this.$router.push({path:'work'}) 
    }
  }
};
</script>
<style scoped>
#Header {
  /* padding: 30px 110px 0 150px; */
  width: 85%;
  margin: 10px auto;
}

#word {
  margin-left: 45%;
  margin-top: -35px;
  margin-bottom: 37px;
  height: 60px;
  line-height: 3.2em;
  letter-spacing: 8px;
}

h1 {
  /*text-align: center;*/
  color: #21b3b9;
  letter-spacing: 30px;
  font-size: 2.3em;
}

.el-menu-demo {
  width: 100%;
  margin: 0px auto;
  padding: 0px auto;
}

.top-left-edition span i {
  float: left;
  margin-right: 10px;
}

i,
input,
label {
  vertical-align: middle;
}

i {
  border: 0;
  display: block;
  cursor: pointer;
}

.top-left-edition span {
  float: left;
  font-size: 16px;
  color: #999999;
  line-height: 24px;
  margin-right: 40px;
}
</style>


