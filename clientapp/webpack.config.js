const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { VueLoaderPlugin } = require('vue-loader');

module.exports = {
  entry: './src/router/index.js', // Adjust the entry point as needed
  output: {
    path: path.resolve(__dirname, 'clientapp/dist'),
    filename: 'static/[name].[contenthash].js',
    clean: true, // Clean the output directory before emit
  },
  module: {
    rules: [
      {
        test: /\.css$/,
        use: ['style-loader', 'css-loader'],
      },
      {
        test: /\.(js|jsx)$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
        },
      },
      {
        test: /\.vue$/,
        loader: 'vue-loader',
      },
      {
        test: /\.(png|jpe?g|gif|svg)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[hash].[ext]',
              outputPath: 'assets',
            },
          },
        ],
      },
    ],
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: './src/index.html',
      filename: '../index.html', // Output to the root of dist
    }),
    new VueLoaderPlugin(),
  ],
  resolve: {
    extensions: ['.js', '.jsx', '.vue'],
    alias: {
      'vue$': 'vue/dist/vue.esm.js',
    },
  },
};