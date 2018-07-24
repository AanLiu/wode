# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:07:19 2018

@author: user
"""

import urllib.request as r
data=r.urlopen('http://api.openweathermap.org/data/2.5/weather?q=tongren&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996').read().decode('utf-8','ignore')
import json
data=json.loads(data)
print(data['main']['temp'])
print(data['main']['pressure'])
print(data['weather'][0]['description'])