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

PORT="/dev/ttyACM0"
SUDO=""
PROXY=""

while getopts p:sr:h OPT
do
    case ${OPT} in
        p)
            PORT="${OPTARG}"
            ;;
        s)
            SUDO="sudo"
            ;;
        r)
            PROXY="--out=udp:${OPTARG}"
            ;;
        h)
            echo "Usage:
    ./mav-proxy.sh -[p:sr:h]
    -p  specify port, '/dev/ttyACM0'
    -s  use 'sudo' or not
    -r  proxy data to QGC/Mission Planner or not, 
        default is '192.168.199.246:14550'
    -h  help"
            ;;
        *)
            echo "Invalid choice."
            exit 1
            ;;
    esac
done

source venv/bin/activate

# Run mavproxy
${SUDO} mavproxy.py --master=${PORT} \
                 ${PROXY} \
                 --out=127.0.0.1:14550

# Select mission