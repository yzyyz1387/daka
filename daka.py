# python3
# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 23:17
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : 打卡s.py
# @Software: PyCharm
import http.cookiejar
import os
import time
import urllib.parse
import urllib.request
from os.path import dirname

date = time.strftime('%Y%m%d')
LOGIN_URL = r'https://app.nwafu.edu.cn/uc/wap/login/check'  # 登录教务系统的URL,目的是获取cookie
get_url = 'https://app.nwafu.edu.cn/ncov/wap/default/save'  # 利用cookie请求打卡地址
headers = {'authority': 'app.nwafu.edu.cn', 'pragma': 'no-cache', 'cache-control': 'no-cache',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
           'sec-fetch-dest': 'document',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
           'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate',
           'referer': 'https://app.nwafu.edu.cn/site/applicationSquare/index?sid=8',
           'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', }

infor = open("./1.txt", encoding='utf-8', errors='ignore')
infor = eval(infor.read())

data = {
    'zgfxdq': '0',
    'mjry': '0',
    'csmjry': '0',
    'tw': '2',
    'sfcxtz': '0',
    'sfjcbh': '0',
    'sfcxzysx': '0',
    'qksm': '',
    'sfyyjc': '0',
    'jcjgqr': '0',
    'remark': '',
    'address': '',
    'geo_api_info': [
        {
            "type": "complete",
            "position": [
                {
                    "Q": "",
                    "R": "",
                    "lng": "",
                    "lat": "",
                }],
            "location_type": "html5",
            "message": "Get ipLocation failed.Get geolocation success.Convert Success.Get address success.",
            "accuracy": 72,
            "isConverted": 'true',
            "status": 1,
            "addressComponent": [
                {
                    "citycode": "",
                    "adcode": "",
                    "businessAreas": [],
                    "neighborhoodType": "",
                    "neighborhood": "",
                    "building": "",
                    "buildingType": "",
                    "street": "",
                    "streetNumber": "",
                    "country": "中国",
                    "province": "",
                    "city": "",
                    "district": "",
                    "township": "",
                }],
            "formattedAddress": "",
            "roads": [],
            "crosses": [],
            "pois": [],
            "info": "SUCCESS",
        }],

    'area': '',
    'province': '',
    'city': '',
    'sfzx': '1',
    'sfjcwhry': '0',
    'sfjchbry': '0',
    'sfcyglq': '0',
    'gllx': '',
    'glksrq': '',
    'jcbhrq': '',
    'bztcyy': '4',
    'sftjhb': '0',
    'sftjwh': '0',
    'jcjg': '',
    'date': date,
    'uid': '77567',
    'created': '1623255995',
    'jcqzrq': '',
    'sfjcqz': '',
    'szsqsfybl': '0',
    'sfsqhzjkk': '0',
    'sqhzjkkys': '',
    'sfygtjzzfj': '0',
    'gtjzzfjsj': '',
    'fxyy': '',
    'id': '19024485',
    'gwszdd': '',
    'sfyqjzgc': '',
    'jrsfqzys': '',
    'jrsfqzfy': '',
    'ismoved': '0',
    'jcbhlx': ''
}
# 计数器
dkCount = 0
errorCount = 0
errorPass = 0

# 遍历字典 学号为key 修改相应data数据
for sn in infor:
    # 最外层信息
    # try:
    data['address'] = infor[sn][0]['address']
    data['area'] = infor[sn][0]['area']
    data['city'] = infor[sn][0]['city']
    data['province'] = infor[sn][0]['province']
    data['sfzx'] = infor[sn][0]['sfzx']
    # geo_api 经纬信息
    data['geo_api_info'][0]['position'][0]['lng'] = infor[sn][0]['lng']
    data['geo_api_info'][0]['position'][0]['lat'] = infor[sn][0]['lat']
    data['geo_api_info'][0]['position'][0]['R'] = infor[sn][0]['lng']
    data['geo_api_info'][0]['position'][0]['Q'] = infor[sn][0]['lat']
    # geo_api 地址信息（内）
    data['geo_api_info'][0]['addressComponent'][0]['adcode'] = infor[sn][0]['adcode']
    data['geo_api_info'][0]['addressComponent'][0]['province'] = infor[sn][0]['province']
    data['geo_api_info'][0]['addressComponent'][0]['city'] = infor[sn][0]['city']
    data['geo_api_info'][0]['addressComponent'][0]['district'] = infor[sn][0]['district']
    # geo_api 地址信息（外）
    data['geo_api_info'][0]['formattedAddress'] = infor[sn][0]['address']

    values = {
        'username': sn,
        'password': infor[sn][0]['password'],
    }
    postdata = urllib.parse.urlencode(values).encode()
    if not os.path.exists(dirname(__file__) + '/cookies/'):
        os.mkdir(dirname(__file__) + '/cookies/')
    # 设置储存cookies的文件
    cookie_filename = './cookies/' + sn + 'cookie_jar.txt'
    cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie_jar)
    opener = urllib.request.build_opener(handler)

    request = urllib.request.Request(LOGIN_URL, postdata, headers)
    try:
        response = opener.open(request)
        # print(response.read().decode())
    except urllib.error.URLError as e:
        print(e.code, ':', e.reason)

    cookie_jar.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到'学号+cookie.txt'中
    # 开始打卡
    data1 = urllib.parse.urlencode(data).encode()
    get_request = urllib.request.Request(get_url, headers=headers, data=data1)
    get_response = opener.open(get_request)
    final = get_response.read().decode()
    if "成功" in final or "已经" in final:
        print(sn, final)
        dkCount += 1
        time.sleep(1)
    elif "为空" in final:
        print(sn, "信息不能为空")
        errorCount += 1
    else:
        print(sn, "账号密码不匹配")
        errorPass += 1

print("完成,打卡数：", dkCount, "错误数：", errorCount, "账号密码错误：", errorPass)
