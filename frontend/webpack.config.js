const isDevelopment = (process.env.DEBUG || "false").toLowerCase() == "true";

const path = require('path');

module.exports = {
  mode: isDevelopment ? "development" : "production",

  entry: './src/index.js',

  output: {
    path: path.resolve('../backend/static'),
    filename: "[name].js",
    clean: true,
    publicPath: isDevelopment ? 'http://localhost:9091/' : '/static',
  },
};

