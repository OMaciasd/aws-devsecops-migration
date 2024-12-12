#!/bin/bash

aws ecr create-repository --repository-name lab-docker-repo
docker build -t lab-docker-app .
docker tag lab-docker-app:latest <account-id>.dkr.ecr.<region>.amazonaws.com/lab-docker-repo:latest
aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account-id>.dkr.ecr.<region>.amazonaws.com
docker push <account-id>.dkr.ecr.<region>.amazonaws.com/lab-docker-repo:latest
