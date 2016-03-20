#coding=utf-8
#qpy:console
#qpy:2
__author__ 'LR'
import site
import json
import os
from androidhelper import Android
import time
try:
    from urllib.request import urlopen
except:
    from urllib2 import urlopen
import base64

d=Android()
os.system('clear')

def gps():
    #开始gps监测
    d.startLocating()

    #获得最新gps定位
    gps=d.getLastKnownLocation().result['passive']

    #gps经度
    lngx=gps['longitude']

    #gps纬度
    lngy=gps['latitude']

    #解决位置偏移，gps坐标系转百度坐标系
    ur='http://api.map.baidu.com/ag/coord/convert?from=0&to=4&x='+str(lngx)+'&y='+str(lngy)
    f=urlopen(ur).read()
    f=json.loads(f)

    #转换后百度坐标系需要base64解码
    lngx=base64.b64decode(f['x'])
    lngy=base64.b64decode(f['y'])
    lngx=lngx
    lngy=lngy


    #聚合接口，根据经纬度返回位置信息
    url='http://lbs.juhe.cn/api/getaddressbylngb?lngx='+str(lngx)+'&lngy='+str(lngy)

    g=urlopen(url).read()
    g=json.loads(g)
    addr=g['row']['result']['formatted_address']

    return addr.encode('utf-8')

    #停止gps监测
    d.stopLocating()

a=gps()
print(a)
