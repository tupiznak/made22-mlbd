#!/bin/bash

apt update -y \
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