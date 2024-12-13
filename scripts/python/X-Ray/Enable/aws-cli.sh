#!/bin/bash
yum install -y aws-xray-daemon
systemctl start xray
