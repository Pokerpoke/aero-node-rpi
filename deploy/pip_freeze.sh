#!/bin/bash
################################################################################
# 
# Copyright (c) 2019 NUAA AeroLab
# 
# @author   Jiang Yang (pokerpoke@qq.com)
# @date     2019-03
# @brief    
# @version  0.0.1
# 
# Last Modified:  2019-03-07
# Modified By:    Jiang Yang (pokerpoke@qq.com)
# 
################################################################################
set -e
# get scripts path
SCRIPT_DIR=$(dirname $(readlink -f $0))
cd ${SCRIPT_DIR}/..
PROJECT_DIR=$(pwd)
cd ${PROJECT_DIR}

source ./venv/bin/activate

pip freeze > requirements.txt