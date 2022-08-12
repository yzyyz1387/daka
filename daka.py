# python3
# -*- coding: utf-8 -*-
# @Time    : 2022/8/12 22:55
# @Author  : yzyyz
# @Email   :  youzyyz1384@qq.com
# @File    : daka.py
# @Software: PyCharm


import json
import time
import httpx
from log import log
from typing import Dict, Optional


date = time.strftime('%Y%m%d')
LOGIN_URL = r'https://app.nwafu.edu.cn/uc/wap/login/check'  # 登录app系统的URL,目的是获取cookie
get_url = 'https://app.nwafu.edu.cn/ncov/wap/default/save'  # 利用cookie请求打卡地址
headers = {'authority': 'app.nwafu.edu.cn', 'pragma': 'no-cache', 'cache-control': 'no-cache',
           'upgrade-insecure-requests': '1',
           'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/80.0.3987.149 Safari/537.36',
           'sec-fetch-dest': 'document',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,'
                     'application/signed-exchange;v=b3;q=0.9',
           'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate',
           'referer': 'https://app.nwafu.edu.cn/site/applicationSquare/index?sid=8',
           'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7', }
infor = json.loads(open("info.json", encoding='utf-8', errors='ignore').read())
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
            "message": "Get+geolocation+success.Convert+Success.Get+address+success.",
            "accuracy": 431,
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
    'uid': '',
    'created': '',
    'jcqzrq': '',
    'sfjcqz': '',
    'szsqsfybl': '0',
    'sfsqhzjkk': '0',
    'sqhzjkkys': '',
    'sfygtjzzfj': '0',
    'gtjzzfjsj': '',
    'fxyy': '',
    'id': '114514',
    'gwszdd': '',
    'sfyqjzgc': '',
    'jrsfqzys': '',
    'jrsfqzfy': '',
    'ismoved': '0',
    'jcbhlx': ''
}


async def main():
    dkCount = 0
    errorCount = 0
    errorPass = 0
    log().info('开始执行')
    for sn in infor:
        values = {
            'username': sn,
            'password': infor[sn][0]['password']
        }
        result = (await daka_async(values))
        if result == 1:
            dkCount += 1
        elif result == 0:
            errorCount += 1
        elif result == -1:
            errorPass += 1
    log().info(f'执行完毕，打卡成功 {dkCount} 人，失败 {errorCount} 人，密码错误 {errorPass} 人')


async def daka_async(values: dict) -> Optional[int]:
    """
    针对提供的values信息进行登录与打卡
    :param values: 包含账号密码的信息
    :return: 1：打卡成功， 0：打卡失败， -1：账号密码错误
    """
    sn = values["username"]
    async with httpx.AsyncClient() as client:
        login = (await client.post(LOGIN_URL, data=values, headers=headers))
        log().debug("登录返回信息： " + login.text)
        login_status: dict = json.loads(login.text)
        message = login_status['m']
        if message == "操作成功":
            log().info(sn + "-----登陆成功")
            data_ = (await produce_data(infor, sn))
            daka_post = (await client.post(get_url, data=data_, headers=headers))
            daka_status = json.loads(daka_post.text)
            log().debug("打卡返回信息：  " + daka_post.text)
            daka_message = daka_status["m"]
            if "成功" in daka_message:
                log().info(sn + "-----打卡成功")
                return 1
            elif "为空" in daka_message:
                log().error(sn + "-----部分数据为空，可开启debug模式查看具体数据")
                log().debug("您提交的数据如下")
                log().debug(data_)
                return 0
            elif "已经" in daka_message:
                log().info(sn + "-----今日已经填报过了")
                return 1
        elif message == "账号或密码错误":
            log().error(sn + "-----账号或密码错误")
            return -1
        elif message == "错误次数已达最大上限,请稍后再试":
            log().error(sn + "-----错误次数已达最大上限,请稍后再试")


async def produce_data(info: dict, sn: str) -> Dict:
    """
    根据提供的信息生成打卡数据
    :param info: 本地数据的字典对象
    :param sn: 学号字符串
    :return: 更新后的字典对象
    """
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
    return data


if __name__ == '__main__':
    log().info("本程序仅供学习使用，请遵守相关法律、规定，珍爱生命！对自己和他人负责！")
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
