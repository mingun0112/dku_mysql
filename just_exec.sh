#!/bin/bash
sudo docker exec -it mysql-container mysql -u root -p1234 -h localhost
python3 main.py