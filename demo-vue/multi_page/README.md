# multi_page

验证vue-cli的多页面打包功能
- 可以比较好的实现多页面
- 需要补充多页面打包公共依赖的splitChunks规则
  - 模块1的公共依赖有修改，不能影响到模块2。就是说模块1修改后，dist中的模块2相关文件的hash值不能被改变
  - 模块1的公共依赖有修改，公共chunks最好不要改变。否则所有模块需要同时更新公共chunks的引入文件名
  - 可以细分公共chunks，保持chunks的稳定性。每个模块能按需加载
  - 公共chunks有版本更新时，确保所有模块的引入都获得更新

## Project setup
```
yarn install
```

### Compiles and hot-reloads for development
```
yarn serve
```

### Compiles and minifies for production
```
yarn build
```

### Run your unit tests
```
yarn test:unit
```

### Lints and fixes files
```
yarn lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
