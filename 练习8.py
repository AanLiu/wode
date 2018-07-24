# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 17:04:00 2018

@author: Lenovo
"""
################淘宝数据抓取100条
import urllib.request as r#导入联网工具包，名为为r    
f=open('湖北的淘宝数据.txt','a',encoding='utf-8') 
url='https://s.taobao.com/search?q=%E8%A3%99%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E6%B9%96%E5%8C%97&s={}&ajax=true'
for i in range(0,100):
    url1=url.format(i*44)
    try:
        data=r.urlopen(url1).read().decode('utf-8','ignore')
        f.write(data+'\n')
        print('第{}行'.format(i+1))
    except Exception as err:
        print('此行有误')
f.close()