#!/bin/bash

# 1. 시스템 패키지 업데이트
echo "Updating system packages..."
sudo apt update -y

# 2. Python과 pip 설치
echo "Installing Python and pip..."
sudo apt install python3 python3-pip -y
sudo apt-get install mysql-server

echo "Installing required Python packages..."
pip3 install -r requirements.txt
