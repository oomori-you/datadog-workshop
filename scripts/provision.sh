#!/bin/bash
set -eu

# apache
apt-get update
apt-get -y install apache2

# php
add-apt-repository ppa:ondrej/php
apt-get update
apt-get -y install php7.0

# fabric
apt-get update
apt-get -y install fabric
