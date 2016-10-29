#!/bin/bash
set -eu

apt-get update

# git
apt-get -y install git

# apache
apt-get -y install apache2

# ab
apt-get -y install apache2-utils

# php
add-apt-repository ppa:ondrej/php
apt-get update
apt-get -y install php7.0

# composer
curl -sS https://getcomposer.org/installer | sudo php -- --install-dir=/usr/local/bin --filename=composer

# pip
apt-get -y install python-pip

# fabric
apt-get -y install fabric
