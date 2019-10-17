#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""

Copyright (c) 2019 NUAA AeroLab

@file
@author   Jiang Yang (pokerpoke@qq.com)
@date     2019-03
@brief    
@version  0.0.1

Last Modified:  2019-03-07
Modified By:    Jiang Yang (pokerpoke@qq.com)

"""

from flask import (Flask, request, jsonify,
                   render_template, redirect,
                   url_for, session, g)
import UAV


app = Flask(__name__)
app.secret_key = '123456'

uav = UAV.UAV()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/connect')
def connect():
    if not uav.connected:
        uav.connect('udp:127.0.0.1:14550')
    if 'next_page' in session:
        r = session['next_page']
        session['next_page'] = ''
        return redirect(r)
    return redirect('/')


@app.route('/precheck')
def precheck():
    return ('@TODO')


@app.route('/takeoff')
def takeoff():
    if not uav.connected:
        session['next_page'] = '/takeoff'
        return redirect('/connect')
    alt = float(request.args.get('alt', 5))
    uav.takeoff(alt)
    return ('done')


@app.route('/land')
def land():
    if not uav.connected:
        session['next_page'] = '/land'
        return redirect('/connect')
    uav.land()
    return ('done')


@app.route('/goto')
def goto():
    n = float(request.args.get('n', 0))
    e = float(request.args.get('e', 0))
    d = float(request.args.get('d', 0))

    uav.goto(n, e, d)
    return ('done')

@app.route('/goto/<direction>')
def goto_direction(direction):
    if direction == 'north':
        uav.goto(1,0,0)
    elif direction == 'south':
        uav.goto(-1,0,0)
    elif direction == 'east':
        uav.goto(0,1,0)
    elif direction == 'west':
        uav.goto(0,-1,0)
    elif direction == 'down':
        uav.goto(0,0,1)
    elif direction == 'up':
        uav.goto(0,0,-1)
    else:
        return ('bad operation')
    return('done')
    

@app.route('/status')
def status():
    if uav.connected:
        return jsonify(connected=uav.connected,
                    mode=uav.vehicle.mode.name.lower(),
                    pitch=uav.vehicle.attitude.pitch,
                    roll=uav.vehicle.attitude.roll,
                    yaw=uav.vehicle.attitude.yaw,
                    lat=uav.vehicle.location.global_frame.lat,
                    long=uav.vehicle.location.global_frame.lon,
                    alt=uav.vehicle.location.global_frame.alt,
                    armed=uav.vehicle.armed
                    )
    else:
        return jsonify(connected=uav.connected)


@app.route('/update')
def update():
    import subprocess
    cmd = ['git', 'pull']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return (p.stdout.read())


@app.route('/test')
def test():
    import subprocess
    cmd = ['pwd']
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    return (p.stdout.read())


@app.route('/restart')
def restart():
    import os

    cmd = ('sudo supervisorctl restart all')
    os.system(cmd)


@app.route('/proxy')
def proxy():
    import os

    cmd = ('sudo supervisorctl stop mavproxy')
    os.system(cmd)
    cmd = ('sudo supervisorctl start mavproxy-proxy')
    os.system(cmd)
    return ('done')


@app.route('/service_status')
def service_status():
    import psutil

    return jsonify(
        cpu_percent=psutil.cpu_percent(),
        disk_usage=psutil.disk_usage('/').percent,
        ip=psutil.net_if_addrs()['wlan0'][0].address
    )


@app.route('/log/mavproxy')
def log_mavproxy():
    from flask import Response

    with open('log/mavproxy.log', 'r') as f:
        return Response(f, mimetype='text/plain')


@app.route('/log/flaskr')
def log_flask():
    from flask import Response

    with open('log/flaskr.log', 'r') as f:
        return Response(f, mimetype='text/plain')


if __name__ == '__main__':
    app.run()
