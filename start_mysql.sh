#!/bin/bash

# 1. 시스템 패키지 업데이트
echo "Updating system packages..."
sudo apt update -y

sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update


sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# 2. Python과 pip 설치
echo "Installing Python and pip..."
sudo apt install python3 python3-pip -y
# sudo apt-get install mysql-server

echo "Installing required Python packages..."
pip3 install -r requirements.txt

echo "pull mysql"
sudo docker pull mysql
sudo docker run --name mysql-container   -e MYSQL_ROOT_PASSWORD=1234   -d -p 3306:3306   -v $(pwd)/db.sql:/docker-entrypoint-initdb.d/db.sql   mysql:latest  

echo "mysql_초기화중.. 잠시만 기다려 주세요"
sleep 10
echo "db.sql 설치 중"
sleep 10
echo "곧 실행됩니다."
sleep 10

# sudo docker exec -it mysql-container mysql -u root -p1234 -h localhost
python3 main.py