var path = require('path');
var htmlWebpackPlugin = require('html-webpack-plugin')

module.exports = {
  mode: "none",
  // mode: "production",
  entry: {
    'page1': './src/page1/index.js',
    'page2': './src/page2/index.js',
  },
  output: {
    path: path.resolve(__dirname, "dist"),
    filename: "[name].js",
    publicPath: "",
  },
  plugins: [
    // new htmlWebpackPlugin({
    //   template: "./src/page1/index.html",
    //   chunks: ['commondll', 'page1'],
    //   inject: true,
    // }),
    // new htmlWebpackPlugin({
    //   template: "./src/page2/index.html",
    //   chunks: ['commondll', 'page2'],
    //   inject: true,
    // }),
  ],
  optimization: {
    runtimeChunk: false,
    splitChunks: {
      // chunks: 'all',
      cacheGroups: {
        commondll: {
          // test: path.resolve(__dirname, 'src/common/frame.js'),
          test: /[\\/]common[\\/]/,
          priority: 10,
          name: 'commondll',
          chunks: 'all',
          minSize: 1,
          // minChunks: 1,
          // reuseExistingChunk: true,
        }
      }
    }
  },
  cache: false,
}