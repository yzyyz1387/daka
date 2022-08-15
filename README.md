

<details>
  <summary>  <h2>目录</h2> </summary>

<!-- TOC -->
* [自动批量打卡项目]()
  * [项目须知、说明](#须知、说明)
  * [本地信息配置文件info.json](#infojson)
  * [南校区范例](南校区范例)
    * [注意`city`、`province`、`district` 必须带"市、省、区"](#-city--province--district----)
  * [如何运行](#如何运行)
  * [执行结果示例](#执行结果示例)
  * [日志](#日志)
  * [ToDo](#todo)
  * [LICENSE](#license)
  * [注意事项](#注意事项)
<!-- TOC -->

</details>

# 自动批量打卡项目

## 须知、说明
- app系统的地址是 [https://app.nwafu.edu.cn/uc/wap/login](https://app.nwafu.edu.cn/uc/wap/login)  
- 打卡界面的地址是[https://app.nwafu.edu.cn/ncov/wap/default/index](https://app.nwafu.edu.cn/ncov/wap/default/index)
- 环境python3.6+
- 主文件 [`daka.py`](daka_old.py)
- 数据文件 [`info.json`](info.json)
- 获取经纬度及行政区划代码：[https://apis.map.qq.com/jsapi?qt=geoc&addr=地名](https://apis.map.qq.com/jsapi?qt=geoc&addr=地名)
- `2022年8月13日`最新采用异步实现,~~早期代码很拉，将就看~~，仅供学习参考，项目雏形于2021年12月，原址[https://yzyyz.top/archives/eed1cf7f.html](https://yzyyz.top/archives/eed1cf7f.html)
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
## 如何运行
首先克隆项目
```bash
git clone https://github.com/NWAFU-CP/daka.git
````
切换目录
```bash
cd daka
````
对`info.json`中的信息进行配置
再执行daka.py
```bash
python daka.py
````

## 执行结果示例
```
2022-08-13 01:11:58,072-INFO: 本程序仅供学习使用，请遵守相关法律、规定，珍爱生命！对自己和他人负责！
2022-08-13 01:11:58,074-INFO: 开始执行
2022-08-13 01:11:58,398-ERROR: 114514-----账号或密码错误
2022-08-13 01:11:58,755-ERROR: 7355608-----账号或密码错误
2022-08-13 01:11:58,756-INFO: 执行完毕，打卡成功 0 人，失败 0 人，密码错误 2 人
```

## 日志 
DEBUG级别的日志会输出在`daka.log`文件中
INFO级别的日志输出在控制台

## ToDo
- [x] 异步实现
- [x] 日志
## LICENSE
[AGPL-3.0 license](LICENSE)

## 注意事项
仅供学习交流，请遵守防疫规定，勿用于非法用途  
以上
