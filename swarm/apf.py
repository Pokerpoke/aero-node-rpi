#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

Copyright (c) 2019 NUAA AeroLab

@file
@author   Jiang Yang (pokerpoke@qq.com)
@date     2019-03
@brief    
@version  0.0.1

Last Modified:  2019-10-17
Modified By:    Jiang Yang (pokerpoke@qq.com)

"""

import requests
import threading


class Node(object):
    def __init__(self, ip_addr='127.0.0.1', *args, **kwargs):
        self.ip_addr = ip_addr
        self.x = 0
        self.y = 0
        self.z = 0

    def update_position(self):
        pass

    @property
    def x(self):
        return self.x

    @property
    def y(self):
        return self.y

    @property
    def z(self):
        return self.z


class follower(Node):
    pass


class leader(Node):
    pass


def compute_repulsion():
    pass


def compute_attraction():
    pass
