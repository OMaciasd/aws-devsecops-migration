#!/bin/bash

docker build -t my-app .
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin <account_id>.dkr.ecr.us-east-1.amazonaws.com
docker tag my-app:latest <account_id>.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
docker push <account_id>.dkr.ecr.us-east-1.amazonaws.com/my-app:latest
