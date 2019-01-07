#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from flask import (Flask, request, jsonify,
                   render_template, redirect,
                   url_for, session)
from dronekit import connect, VehicleMode
from aerodrone import *


app = Flask(__name__)
app.secret_key = "123456"

vehicle = None
CONNECTED = False


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/connect")
def connect_():
    global vehicle
    global CONNECTED

    # vehicle = connect("127.0.0.1:14550", wait_ready=True)
    vehicle = connect("/dev/ttyACM0", wait_ready=True)
    CONNECTED = True
    if "url" in session:
        return redirect(session["url"])
    return render_template("index.html")


@app.route("/takeoff")
def takeoff():
    global vehicle
    global CONNECTED

    if not CONNECTED:
        session["url"] = "/takeoff"
        return redirect("/connect")

    vehicle.mode = VehicleMode("GUIDED")

    arm_and_take_off(vehicle, 5)

    return "done".encode("utf-8")


@app.route("/land")
def land():
    global vehicle
    global CONNECTED

    vehicle.mode = VehicleMode("LAND")
    vehicle.close()
    CONNECTED = False

    return "done".encode("utf-8")


@app.route("/goto")
def goto_():
    global vehicle
    global CONNECTED

    if not CONNECTED:
        vehicle = connect("127.0.0.1:14550", wait_ready=True)
        CONNECTED = True

    n = float(request.args.get("n", 0))
    e = float(request.args.get("e", 0))
    d = float(request.args.get("d", 0))

    if d != 0:
        goto(vehicle, n, e, d)
    else:
        goto(vehicle, n, e)

    return "done".encode("utf-8")


@app.route("/status")
def status():
    global vehicle
    global CONNECTED

    if not CONNECTED:
        session["url"] = "/status"
        return redirect("/connect")
    else:
        return jsonify(connect=CONNECTED,
                       mode=vehicle.mode.name.lower(),
                       pitch=vehicle.attitude.pitch,
                       roll=vehicle.attitude.roll,
                       yaw=vehicle.attitude.yaw,
                       lat=vehicle.location.global_frame.lat,
                       long=vehicle.location.global_frame.lon,
                       alt=vehicle.location.global_frame.alt,
                       )


if __name__ == "__main__":
    app.run()
