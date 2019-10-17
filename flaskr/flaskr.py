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


@app.before_request
def before_request():
    g.uav = UAV.UAV()
    # g.uav.connect('127.0.0.1:14550')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/connect')
def connect():
    if not g.uav.connected:
        g.uav.connect('127.0.0.1:14550')
    if 'next_page' in session:
        r = session['next_page']
        session['next_page'] = ''
        return redirect(r)
    return redirect('/')


@app.route('/precheck')
def precheck():
    return


@app.route('/takeoff')
def takeoff():
    if not g.uav.connected:
        session['next_page'] = '/takeoff'
        return redirect('/connect')
    alt = float(request.args.get('alt', 5))
    g.uav.takeoff(alt)
    return ('done')


@app.route('/land')
def land():
    if not g.uav.connected:
        session['next_page'] = '/land'
        return redirect('/connect')
    g.uav.land()
    return ('done')


@app.route('/goto')
def goto():
    n = float(request.args.get('n', 0))
    e = float(request.args.get('e', 0))
    d = float(request.args.get('d', 0))

    g.uav.goto(n, e, d)
    return ('done')


@app.route('/goto_north')
def goto_north():
    n = float(request.args.get('n', 1))
    e = float(request.args.get('e', 0))
    d = float(request.args.get('d', 0))

    g.uav.goto(n, e, d)
    return ('done')


@app.route('/goto_east')
def goto_east():
    n = float(request.args.get('n', 0))
    e = float(request.args.get('e', 1))
    d = float(request.args.get('d', 0))

    g.uav.goto(n, e, d)
    return ('done')


@app.route('/goto_down')
def goto_down():
    n = float(request.args.get('n', 0))
    e = float(request.args.get('e', 0))
    d = float(request.args.get('d', 1))

    g.uav.goto(n, e, d)
    return ('done')


@app.route('/status')
def status():
    # if not g.uav.connected:
    #     session['next_page'] = '/status'
    #     return redirect('/connect')
    if not g.uav.connected:
        return jsonify(connected=g.uav.connected)
    else:
        return jsonify(connected=g.uav.connected,
                    mode=g.uav.vehicle.mode.name.lower(),
                    pitch=g.uav.vehicle.attitude.pitch,
                    roll=g.uav.vehicle.attitude.roll,
                    yaw=g.uav.vehicle.attitude.yaw,
                    lat=g.uav.vehicle.location.global_frame.lat,
                    long=g.uav.vehicle.location.global_frame.lon,
                    alt=g.uav.vehicle.location.global_frame.alt,
                    armed=g.uav.vehicle.armed
                    )


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
