#!/bin/bash

# 1. 시스템 패키지 업데이트
echo "Updating system packages..."
sudo apt update -y

# 2. Python과 pip 설치
echo "Installing Python and pip..."
sudo apt install python3 python3-pip -y
sudo apt-get install mysql-server
# 3. MySQL 데이터베이스 초기화
echo "Installing MySQL database schema from db.sql..."
DB_USER="root"
DB_PASSWORD="1234"
DB_NAME="classdb"
SQL_FILE="db.sql"
sudo service mysql restart
#sudo service mysql restart
# MySQL 명령어로 db.sql 실행
sudo mysql -u $DB_USER < $SQL_FILE
if [ $? -eq 0 ]; then
    echo "Database schema successfully installed."
else
    echo "Failed to install database schema. Please check db.sql or your database settings."
    exit 1
fi

# 4. Python 패키지 설치
echo "Installing required Python packages..."
pip3 install pymysql

# 5. Python 스크립트 실행
echo "Running Python script..."
python3 install_db.py
