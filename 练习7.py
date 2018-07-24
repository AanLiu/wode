# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 17:50:39 2018

@author: Lenovo
"""
url='http://api.openweathermap.org/data/2.5/forecast?q=tongren,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
for i in range(0,34,1):
    a=data['list'][i]['main']['temp']
    print(a)
    if a>20:
        print('气候适宜玩耍') 
    elif a>30:
        print('花晒焉了')
    elif a>35:
        print('狗晒趴了')
    elif a>40:
        print('人晒化了')
    elif a<10:
        print('请注意保暖')
    elif a<0:
        print('请注意防寒')
#############淘宝
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.2&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
for i in range(35):
    if i==3:break
    if i==6:continue
    print('价格:'+data['mods']['itemlist']['data']['auctions'][i]['view_price'])
    print('商品名为:'+data['mods']['itemlist']['data']['auctions'][i]['raw_title'])
    print('已售出:'+data['mods']['itemlist']['data']['auctions'][i]['view_sales'])
    g=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    if g>str(1000):
        print('火爆商品，值得信赖')
    elif g<str(10):
        print('恭喜您成为第一个吃螃蟹的人')
    else:
        print('祝您购物愉快')
   