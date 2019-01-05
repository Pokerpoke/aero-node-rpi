#!/bin/bash
################################################################################
# 
# Copyright (c) 2018 NUAA AeroLab
# 
# @author   Jiang Yang (pokerpoke@qq.com)
# @date     2018-10
# @brief    
# @version  0.0.1
# 
# Last Modified:  2018-10-16
# Modified By:    Jiang Yang (pokerpoke@qq.com)
# 
################################################################################
set -e
# get scripts path
SCRIPT_DIR=$(dirname $(readlink -f $0))
cd ${SCRIPT_DIR}
PROJECT_DIR=$(pwd)
cd ${PROJECT_DIR}

if [[ -z "$1" ]] ; then
    PORT="/dev/ttyACM0"
    SUDO="sudo"
else
    PORT="$1"
    SUDO=""
fi

source venv/bin/activate

# Run mavproxy
${SUDO} mavproxy.py --master=${PORT} \
                 --out=udp:192.168.199.246:14550 \
                 --out=127.0.0.1:14550 \
                 --out=127.0.0.1:14555
                
# Select mission