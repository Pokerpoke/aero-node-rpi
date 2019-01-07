#!/bin/bash
################################################################################
# 
# Copyright (c) 2018 NUAA AeroLab
# 
# @author   Jiang Yang (pokerpoke@qq.com)
# @date     2018-11
# @brief    
# @version  0.0.1
# 
# Last Modified:  2018-11-23
# Modified By:    Jiang Yang (pokerpoke@qq.com)
# 
################################################################################
set -e
# get scripts path
SCRIPT_DIR=$(dirname $(readlink -f $0))
cd ${SCRIPT_DIR}
PROJECT_DIR=$(pwd)
cd ${PROJECT_DIR}

export FLASK_APP=flaskr.py
export FLASK_ENV=development

source venv/bin/activate

export LC_ALL=C.UTF-8
export LANG=C.UTF-8

cd ${PROJECT_DIR}/flaskr

flask run --host=0.0.0.0
