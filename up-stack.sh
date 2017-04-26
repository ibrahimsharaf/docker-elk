#!/bin/bash
# start elastic stack
sudo sysctl -w vm.max_map_count=262144
sudo docker-compose up
