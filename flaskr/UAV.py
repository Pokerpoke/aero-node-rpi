#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

Copyright (c) 2019 NUAA AeroLab

@file
@author   Jiang Yang (pokerpoke@qq.com)
@date     2019-03
@brief    
@version  0.0.1

Last Modified:  2019-10-19
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
        print("Start connect")
        self.vehicle = dronekit.connect(addr, wait_ready=True)
        if self.vehicle == None:
            self.set_connected(False)
        else:
            self.set_connected(True)
        print(self.connected)
        print("Stop connect")
        print("Download commands")
        cmds = self.vehicle.commands
        cmds.download()
        cmds.wait_ready()

    def precheck(self):
        return

    def takeoff(self, alt=5):
        self.vehicle.mode = dronekit.VehicleMode("GUIDED")
        aerodrone.arm_and_take_off(self.vehicle, alt)

    def goto(self, n=0, e=0, d=0):
        if (d == 0):
            aerodrone.goto(self.vehicle, n, e)
        # @TODO:fix relative down
        else:
            aerodrone.goto_position_target_local_ned(self.vehicle, 0, 0, d)

    def land(self):
        self.vehicle.mode = dronekit.VehicleMode("LAND")

    def return_to_land(self):
        self.vehicle.mode = dronekit.VehicleMode("RTL")

    def close(self):
        self.vehicle.close()

    @property
    def alt(self):
        return self.vehicle.location.global_frame.alt

    @property
    def lon(self):
        return self.vehicle.location.global_frame.lon

    @property
    def lat(self):
        return self.vehicle.location.global_frame.lat

    @property
    def is_armable(self):
        return self.vehicle.is_armable

    @property
    def home_alt(self):
        return self.vehicle.home_location.alt

    @property
    def home_lon(self):
        return self.vehicle.home_location.lon

    @property
    def pitch(self):
        return self.vehicle.attitude.pitch

    @property
    def yaw(self):
        return self.vehicle.attitude.yaw

    @property
    def roll(self):
        return self.vehicle.attitude.roll

    @property
    def mode(self):
        return self.vehicle.mode.name

    @property
    def armed(self):
        return self.vehicle.armed

    @property
    def north(self):
        return self.vehicle.location.local_frame.north

    @property
    def east(self):
        return self.vehicle.location.local_frame.east

    @property
    def down(self):
        return self.vehicle.location.local_frame.down
