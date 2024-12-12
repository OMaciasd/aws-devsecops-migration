#!/bin/bash

docker run -d -p 8080:80 <account-id>.dkr.ecr.<region>.amazonaws.com/lab-docker-repo:latest
