## 批量打卡项目
- app系统的地址是 [https://app.nwafu.edu.cn/uc/wap/login](https://app.nwafu.edu.cn/uc/wap/login)  
- 打卡界面的地址是[https://app.nwafu.edu.cn/ncov/wap/default/index](https://app.nwafu.edu.cn/ncov/wap/default/index)
- 环境python3.6+
- 主文件 [`daka.py`](daka_old.py)
- 数据文件 [`info.json`](info.json)
- 获取经纬度及行政区划代码：[https://apis.map.qq.com/jsapi?qt=geoc&addr=地名](https://apis.map.qq.com/jsapi?qt=geoc&addr=地名)
- 早期作品，代码很拉，将就看，仅供学习参考，项目雏形于2021年12月，原址[https://yzyyz.top/archives/eed1cf7f.html](https://yzyyz.top/archives/eed1cf7f.html)
- 将其加入计划任务可实现自动打卡

## [info.json](info.json)
**`key`**: 学号  
**`password`**: 密码  
... ...   
**`sfzx`**： 是否在校 1 在校，0不在校  
**`adcode`**: 行政区划代码  

## 南校区范例
### 注意`city`、`province`、`district` 必须带"市、省、区"
```json
{
    "2019114514": [{

        "password": "114514",
        "address": "陕西省咸阳市杨陵区李台街道G30连霍高速西北农林科技大学南校区",
        "area": "陕西省咸阳市杨陵区",
        "city": "咸阳市",
        "province": "陕西省",
        "district": "杨陵区",
        "sfzx": "1",
        "lng": "108.068236",
        "lat": "34.257315",
        "adcode": "610403" }]
}

```
## 执行结果示例
```
2022-05-20 16:44:49.357832 2019010088 {"e":1,"m":"今天已经填报了","d":{}}
2022-05-20 16:44:50.879155 1234567890 账号密码不匹配
完成,打卡数： 1 错误数： 0 账号密码错误： 1 
 ------------------------------
```

## 日志 
DEBUG级别的日志会输出在`daka.log`文件中
INFO级别的日志输出在控制套

## ToDo
- [x] 异步实现
- [x] 日志
## LICENSE
[AGPL-3.0 license](LICENSE)

## 注意事项
仅供学习交流，请遵守防疫规定，勿用于非法用途
以上
