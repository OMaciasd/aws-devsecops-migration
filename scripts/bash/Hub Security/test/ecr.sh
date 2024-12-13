#!/bin/bash

aws ecr create-repository --repository-name lab-docker-repo
docker build -t vulnerable-image .
docker tag vulnerable-image <account-id>.dkr.ecr.<region>.amazonaws.com/vulnerable-images:v1
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/vulnerable-images:v1
