#!/bin/bash

#echo "deb http://cdn-fastly.deb.debian.org/debian/ jessie main
#deb-src http://cdn-fastly.deb.debian.org/debian/ jessie main
#
#deb http://security.debian.org/ jessie/updates main
#deb-src http://security.debian.org/ jessie/updates main
#
#deb http://archive.debian.org/debian jessie-backports main
#deb-src http://archive.debian.org/debian jessie-backports main
#"  > /etc/apt/sources.list \
#&& echo 'Acquire::Check-Valid-Until "false";' > /etc/apt/apt.conf \
apt update -y \
&& apt install --force-yes -y libsqlite3-0=3.8.7.1-1+deb8u6 \
&& apt install --force-yes -y libssl1.0.0=1.0.1t-1+deb8u12 \
&& apt install -y wget build-essential libreadline-gplv2-dev libncursesw5-dev \
     libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev libffi-dev zlib1g-dev \
&& mkdir -p /opt/python \
&& cd /opt/python \
&& wget -q https://www.python.org/ftp/python/3.10.8/Python-3.10.8.tgz \
&& tar xzf Python-3.10.8.tgz \
&& cd Python-3.10.8 \
&& ./configure --enable-optimizations \
&& make -j10 altinstall \
& /entrypoint.sh /run.sh