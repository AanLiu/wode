# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 18:06:29 2018

@author: user
"""

url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
import urllib.request as r
data=r.urlopen(url).read().decode('utf-8','ignore')
import json
data=json.loads(data)
#天气信息爬取
print('第一天')
print('气温'+str(data['list'][2]['main']['temp']))
print('最低气温'+str(data['list'][2]['main']['temp_min']))
print('最高气温'+str(data['list'][2]['main']['temp_max']))
print('天气状况'+str(data['list'][2]['weather'][0]['main']))
print('气压'+str(data['list'][2]['main']['pressure']))
print('第二天')
print('气温'+str(data['list'][10]['main']['temp']))
print('最低气温'+str(data['list'][10]['main']['temp_min']))
print('最高气温'+str(data['list'][10]['main']['temp_max']))
print('天气状况'+str(data['list'][10]['weather'][0]['main']))
print('气压'+str(data['list'][10]['main']['pressure']))
print('第三天')
print('气温'+str(data['list'][18]['main']['temp']))
print('最低气温'+str(data['list'][18]['main']['temp_min']))
print('最高气温'+str(data['list'][18]['main']['temp_max']))
print('天气状况'+str(data['list'][18]['weather'][0]['main']))
print('气压'+str(data['list'][18]['main']['pressure']))
print('第四天')
print('气温'+str(data['list'][26]['main']['temp']))
print('最低气温'+str(data['list'][26]['main']['temp_min']))
print('最高气温'+str(data['list'][26]['main']['temp_max']))
print('天气状况'+str(data['list'][26]['weather'][0]['main']))
print('气压'+str(data['list'][26]['main']['pressure']))
print('第五天')
print('气温'+str(data['list'][34]['main']['temp']))
print('最低气温'+str(data['list'][34]['main']['temp_min']))
print('最高气温'+str(data['list'][34]['main']['temp_max']))
print('天气状况'+str(data['list'][34]['weather'][0]['main']))
print('气压'+str(data['list'][34]['main']['pressure']))
#英语翻译
input=input('please input city:')
print(str(input))
print('day1')
print('temperature'+str(data['list'][2]['main']['temp']))
print('minimum temperature'+str(data['list'][2]['main']['temp_min']))
print('maximum temperature'+str(data['list'][2]['main']['temp_max']))
print('weather'+str(data['list'][2]['weather'][0]['main']))
print('pressure'+str(data['list'][2]['main']['pressure']))
print('')
print('day2')
print('temperature'+str(data['list'][10]['main']['temp']))
print('minimum temperature'+str(data['list'][10]['main']['temp_min']))
print('maximum temperature'+str(data['list'][10]['main']['temp_max']))
print('weather'+str(data['list'][10]['weather'][0]['main']))
print('pressure'+str(data['list'][10]['main']['pressure']))
print('')
print('day3')
print('temperature'+str(data['list'][18]['main']['temp']))
print('minimum temperature'+str(data['list'][18]['main']['temp_min']))
print('maximum temperature'+str(data['list'][18]['main']['temp_max']))
print('weather'+str(data['list'][18]['weather'][0]['main']))
print('pressure'+str(data['list'][18]['main']['pressure']))
print('')
print('day4')
print('temperature'+str(data['list'][26]['main']['temp']))
print('minimum temperature'+str(data['list'][26]['main']['temp_min']))
print('maximum temperature'+str(data['list'][26]['main']['temp_max']))
print('weather'+str(data['list'][26]['weather'][0]['main']))
print('pressure'+str(data['list'][26]['main']['pressure']))
print('')
print('day5')
print('temperature'+str(data['list'][34]['main']['temp']))
print('minimum temperature'+str(data['list'][34]['main']['temp_min']))
print('maximum temperature'+str(data['list'][34]['main']['temp_max']))
print('weather'+str(data['list'][34]['weather'][0]['main']))
print('pressure'+str(data['list'][34]['main']['pressure']))
print('')


#折线图

a=data['list'][2]['main']['temp']
b=data['list'][10]['main']['temp']
c=data['list'][18]['main']['temp']
d=data['list'][26]['main']['temp']
e=data['list'][34]['main']['temp']
print('温度折线图')
print('第一天:' + '-'*int(a))
print('第二天:' + '-'*int(b))
print('第三天:' + '-'*int(c))
print('第四天:' + '-'*int(d))
print('第五天:' + '-'*int(e))
#排序
print('温度排序')
sorted([a,b,c,d,e])
