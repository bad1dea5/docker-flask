//
//
//

const path = require('path');
const webpack = require('webpack');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');

const Build = process.env.NODE_ENV === 'production' ? 'production' : 'development'

module.exports = {
    context: __dirname,
    entry: {
        default_js: path.join(__dirname, 'assets', 'js', 'default'),
        default_css: [
            path.join(__dirname, 'node_modules', 'line-awesome', 'dist', 'line-awesome', 'css', 'line-awesome.css'),
            path.join(__dirname, 'node_modules', 'bootstrap', 'dist', 'css', 'bootstrap.css'),
            path.join(__dirname, 'assets', 'scss', 'default'),
        ],
    },
    mode: Build,
    output: {
        filename: "[name].bundle.js",
        path: path.join(__dirname, "app", "static", "build"),
    },
    resolve: {
        extensions: [".js", ".jsx", ".scss", ".css"],
    },
    plugins: [
        new MiniCssExtractPlugin({ filename: "[name].bundle.css" }),
        new webpack.ProvidePlugin({ $: "jquery", jQuery: "jquery" }),
    ],
    module: {
        rules: [
            {
                test: /\.s[ac]ss$/i,
                use: [
                    { loader: MiniCssExtractPlugin.loader },
                    "css-loader",
                    {
                        loader: "sass-loader",
                        options: {
                            implementation: require("sass")
                        },
                    },
                ],
            },
            {
                test: /\.css$/,
                use: [
                    { loader: MiniCssExtractPlugin.loader },
                    "css-loader"
                ],
            },
            {
                test: /\.js(x)$/i,
                exclude: /node_modules/,
                use: [
                    {
                        loader: "babel-loader",
                        options: {
                            presets: ["@babel/preset-env"],
                            cacheDirectory: true,
                        },
                    },
                ],
            },
            {
                test: /\.(svg|png|jpe?g|gif|ico)(\?.*)?$/i,
                type: "asset/resource",
                generator: { filename: "img/[name][ext]" },
            },
            {
                test: /\.(woff2|ttf|eot)(\?.*)?$/i,
                type: "asset",
                generator: { filename: "font/[name][ext]" },
            }
        ],
    },
};
