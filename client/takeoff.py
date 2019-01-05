#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

Copyright (c) 2019 NUAA AeroLab

@file
@author   Jiang Yang (pokerpoke@qq.com)
@date     2019-01
@brief    
@version  0.0.1

Last Modified:  2019-01-04
Modified By:    Jiang Yang (pokerpoke@qq.com)

"""
import requests
import threading

targets = ["127.0.0.1",
           "192.168.0.9"]
urls = []

for target in targets:
    url = "http://" + target + ":5000/takeoff"
    urls.append(url)

print(urls)


def takeoff(url):
    r = requests.get(url)
    print(r.text)


threads = []

for url in urls:
    threads.append(threading.Thread(target=takeoff(url)))
    threads[-1].setDaemon(True)
    threads[-1].start
