module.exports = {
  css: {
    loaderOptions: {
      sass: {
        prependData: `@import "./src/assets/index.scss";`
      }
    }
  }
};
