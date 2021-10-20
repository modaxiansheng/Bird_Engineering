import axios from 'axios';
// 开发：
const http = axios.create({
  baseURL: window.location.origin + '/api'
});
// 生产：
// const http = axios.create();

http.interceptors.response.use(function (response) {
  // 对响应数据做点什么
  return response.data;
}, function (error) {
  // 对响应错误做点什么
  return Promise.reject(error);
});

export default http;
