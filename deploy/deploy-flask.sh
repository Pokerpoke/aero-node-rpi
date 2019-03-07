#!/usr/bin/env bash
################################################################################
# 
# Copyright (c) 2018 NUAA AeroLab
# 
# @author   Jiang Yang (pokerpoke@qq.com)
# @date     2018-11
# @brief    
# @version  0.0.1
# 
# Last Modified:  2018-11-22
# Modified By:    Jiang Yang (pokerpoke@qq.com)
# 
################################################################################
set -e
# get scripts path
SCRIPT_DIR=$(dirname $(readlink -f $0))
cd ${SCRIPT_DIR}/..
PROJECT_DIR=$(pwd)
cd ${PROJECT_DIR}

sudo apt-get update
sudo apt-get install -y supervisor python3-venv iftop

sudo cp ${PROJECT_DIR}/supervisor/supervisord.conf /etc/supervisor/supervisord.conf

python3 -m venv venv

source ./venv/bin/activate

pip install -r requirements.txt
