const path = require('path');
function resolve (dir) {
  return path.resolve(__dirname, dir);
}

module.exports = {
  css: {
    loaderOptions: {
      less: {
        javascriptEnabled: true
      }
    }
  },
  chainWebpack: config => {
    config.resolve.alias
      .set('@', resolve('src'));
  },
  devServer: {
    proxy: {
      '/api': {
        target: 'http://localhost:5000',
        pathRewrite: { '/api': '' },
        secure: false
      }
    }
  }
};
