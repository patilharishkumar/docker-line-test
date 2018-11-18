#!/bin/bash
#sudo curl -L "https://github.com/docker/compose/releases/download/1.22.0/docker-compose-$(uname -s)-$(uname -m)"  -o /usr/local/bin/docker-compose
#sudo mv ./docker-compose /usr/bin/docker-compose
#sudo chmod +x /usr/bin/docker-compose
#sudo apt-get install docker-compose
#sudo pip install docker-compose

docker-compose rm
docker-compose stop
docker-compose build
docker-compose up --scale app=$1 -d
