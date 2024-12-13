#!/bin/bash

docker run -d -p 8080:80 -e AWS_XRAY_DAEMON_ADDRESS=127.0.0.1:2000 \
    amazon/aws-xray-daemon
