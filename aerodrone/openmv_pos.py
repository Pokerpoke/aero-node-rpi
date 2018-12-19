#!/usr/bin/env python
# -*- coding:utf-8 -*-


class OpenMV_POS:
    x = 0.0
    v_x = 0.0
    a_x = 0.0
    y = 0.0
    v_y = 0.0
    a_y = 0.0
    updated = False

    def __init__(self, *args, **kwargs):
        self.x = 0.0
        self.v_x = 0.0
        self.a_x = 0.0
        self.y = 0.0
        self.v_y = 0.0
        self.a_x = 0.0

    def to_origin():
        return math.sqrt(x * x + y * y)

    def line_speed():
        return math.sqrt(v_x * v_x + v_y * v_y)

    def line_acceleration():
        return math.sqrt(a_x * a_x + a_y * a_y)
