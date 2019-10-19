#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

Copyright (c) 2019 NUAA AeroLab

@file
@author   Jiang Yang (pokerpoke@qq.com)
@date     2019-10
@brief    
@version  0.0.1

Last Modified:  2019-10-18
Modified By:    Jiang Yang (pokerpoke@qq.com)

"""

import requests
import math
import json


class Config(object):
    def __init__(self, *args, **kwargs):
        self.configs = self.read_config()

    def read_config(self, config_file='swarm_config.json'):
        with open(config_file) as f:
            j = json.load(f)
        return j


c = Config()


def get_d_ned(p1, p2):
    earth_radius = 6378137.0

    d_lat = p2.lat - p1.lat
    d_lon = p2.lon - p1.lon
    d_n = d_lat * earth_radius
    d_e = d_lon * earth_radius * math.cos(p1.lat * math.pi / 180)
    return d_n, d_e


def get_leader_status():
    leader_url = 'http://' + str(c.configs['leader_ip']) + ':5000'
    r = requests.get(leader_url + '/status')
    if not r.json()['connected']:
        r = requests.get(leader_url + '/connect')
    r = requests.get(leader_url + '/status')
    print(r.json())


def get_leader_home_position():
    r = requests.get('http://' + str(c.configs['leader_ip']) + ':5000/status')
    print(r.json())


def get_leader_position():
    pass


if __name__ == "__main__":
    get_leader_status()
    requests.get('http://' + str(c.configs['leader_ip']) + ':5000/takeoff')
    requests.get('http://' + str(c.configs['leader_ip']) + ':5000/goto/east')
    get_leader_status()
