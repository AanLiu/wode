# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:18:03 2018

@author: Lenovo
"""

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
#天气
def day(a,b):
    print('第'+str(a)+'天气预报:')
    print('气温'+str(data['list'][b]['main']['temp']))
    print('最低气温'+str(data['list'][b]['main']['temp_min']))
    print('最高气温'+str(data['list'][b]['main']['temp_max']))
    print('天气状况'+str(data['list'][b]['weather'][0]['main']))
    print('气压'+str(data['list'][b]['main']['pressure']))
day(1,2)
day(2,10)
day(3,18)
day(4,26)
day(5,34)
    
#温度折线图
def  clac(s):   
     return '-'*int (data['list'][s]['main']['temp'])

print('温度折线图')
print('第一天:' ,clac(2))
print('第二天:' ,clac(10))
print('第三天:' ,clac(18))
print('第四天:' ,clac(26))
print('第五天:' ,clac(34))
#气温排序
def chart(o):
    g=[data['list'][o]['main']['temp']]
    return g
m1=chart(2)
m2=chart(10)
m3=chart(18)
m4=chart(26)
m5=chart(34)
sl=[m1,m2,m3,m4,m5]
print('五天天气温度升序排序')
print(sorted(sl))