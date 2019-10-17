#!/usr/bin/env python2
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

import dronekit
import aerodrone


class UAV(object):
    def __init__(self, *args, **kwargs):
        self.connected = False
        self.vehicle = None

    def set_connected(self, flag):
        self.connected = flag

    def connect(self, addr):
        print("start connect")
        self.vehicle = dronekit.connect(addr, wait_ready=True)
        if self.vehicle == None:
            self.set_connected(False)
        else:
            self.set_connected(True)
        print(self.connected)
        print("stop connect")

    def precheck(self):
        return

    def takeoff(self, alt=5):
        self.vehicle.mode = dronekit.VehicleMode("GUIDED")
        aerodrone.arm_and_take_off(self.vehicle, alt)

    def goto(self, n=0, e=0, d=0):
        if (d==0):
            aerodrone.goto(self.vehicle, n, e)
        else:
            # aerodrone.send_ned_velocity(self.vehicle,0,0,d,1)
            aerodrone.goto_position_target_local_ned(self.vehicle,
                                      self.vehicle.location.global_frame.lat, 
                                       self.vehicle.location.global_frame.lon, 
                                       self.vehicle.location.global_frame.alt + d)
            # self.vehicle.commands.goto(LocationGlobal(self.vehicle.location.global_frame.lat, 
            #                            self.vehicle.location.global_frame.lon, 
            #                            self.vehicle.location.global_frame.alt + d))

    def land(self):
        self.vehicle.mode = dronekit.VehicleMode("LAND")

    def return_to_land(self):
        self.vehicle.mode = dronekit.VehicleMode("RTL")

    def close(self):
        self.vehicle.close()
