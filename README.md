## 批量打卡项目
- app系统的地址是 [https://app.nwafu.edu.cn/uc/wap/login](https://app.nwafu.edu.cn/uc/wap/login)  
- 打卡界面的地址是[https://app.nwafu.edu.cn/ncov/wap/default/index](https://app.nwafu.edu.cn/ncov/wap/default/index)
- 环境python3.6+
- 主文件 [`daka.py`](daka.py)
- 数据文件 [`info.json`](info.json)
- 获取经纬度及行政区划代码：[https://apis.map.qq.com/jsapi?qt=geoc&addr=地名](https://apis.map.qq.com/jsapi?qt=geoc&addr=地名)
- 早期作品，代码很拉，将就看，仅供学习参考，项目雏形于2021年12月，原址[https://yzyyz.top/archives/eed1cf7f.html](https://yzyyz.top/archives/eed1cf7f.html)
- 将其加入计划任务可实现自动打卡

## [info.json](info.json)
**`key`**: 学号  
**`password`**: 密码  
...  
**`sfzx`**： 是否在校 1 在校，0不在校  
**`adcode`**: 行政区划代码  

## ToDo
- [ ] 异步实现

## LICENSE
[AGPL-3.0 license](LICENSE)

## 注意事项
仅供学习交流，请遵守防疫规定，勿用于非法用途
以上
