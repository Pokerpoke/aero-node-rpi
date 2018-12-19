#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from flask import Flask, request
from dronekit import connect, VehicleMode
from aerodrone import *


app = Flask(__name__)

vehicle = []
CONNECTED = False


@app.route("/")
def index():
    return "hello".encode("utf-8")


@app.route("/connect")
def connect_():
    global vehicle

    vehicle = connect("127.0.0.1:14555", wait_ready=True)
    return "done".encode("utf-8")


@app.route("/takeoff")
def takeoff():
    global vehicle

    if (not CONNECTED):
        vehicle = connect("127.0.0.1:14555", wait_ready=True)

    arm_and_take_off(vehicle, 5)

    return "done".encode("utf-8")


@app.route("/land")
def land():
    global vehicle

    vehicle.mode = VehicleMode("LAND")
    vehicle.close()

    return "done".encode("utf-8")
