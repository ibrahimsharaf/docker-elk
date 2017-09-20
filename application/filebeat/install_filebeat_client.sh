#!/bin/bash

set -e

# https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html
curl -L -O https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-6.0.0-beta2-amd64.deb
dpkg -i filebeat-6.0.0-beta2-amd64.deb
rm -rf filebeat-6.0.0-beta2-amd64.deb
