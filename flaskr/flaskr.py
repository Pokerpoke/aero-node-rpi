#!/usr/bin/env python2
# -*- coding:utf-8 -*-

from flask import (Flask, request, jsonify,
                   render_template, redirect,
                   url_for, session)
import UAV


app = Flask(__name__)
app.secret_key = "123456"

uav = UAV.UAV()
uav.connect("127.0.0.1:14550")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/precheck")
def precheck():
    return


@app.route("/takeoff")
def takeoff():
    alt = float(request.args.get("alt", 5))
    uav.takeoff(alt)
    return ("hello")


@app.route("/land")
def land():
    uav.land()
    return ("hello")


@app.route("/goto")
def goto():
    n = float(request.args.get("n", 0))
    e = float(request.args.get("e", 0))
    d = float(request.args.get("d", 0))

    uav.goto(n, e, d)
    return ("hello")


@app.route("/status")
def status():
    return jsonify(connect=uav.connected,
                   mode=uav.vehicle.mode.name.lower(),
                   pitch=uav.vehicle.attitude.pitch,
                   roll=uav.vehicle.attitude.roll,
                   yaw=uav.vehicle.attitude.yaw,
                   lat=uav.vehicle.location.global_frame.lat,
                   long=uav.vehicle.location.global_frame.lon,
                   alt=uav.vehicle.location.global_frame.alt,
                   armed=uav.vehicle.armed
                   )


if __name__ == "__main__":
    app.run()
