#!/bin/bash

# Script to setup basic AWS resources

# Set AWS region (you can change it to your desired region)
AWS_REGION="us-east-1"

# Create VPC
echo "Creating VPC..."
VPC_ID=$(aws ec2 create-vpc --cidr-block 10.0.0.0/16 --region $AWS_REGION --query 'Vpc.VpcId' --output text)
echo "VPC created with ID: $VPC_ID"

# Create Subnet
echo "Creating Subnet..."
SUBNET_ID=$(aws ec2 create-subnet --vpc-id $VPC_ID --cidr-block 10.0.1.0/24 --region $AWS_REGION --query 'Subnet.SubnetId' --output text)
echo "Subnet created with ID: $SUBNET_ID"

# Create Internet Gateway
echo "Creating Internet Gateway..."
IGW_ID=$(aws ec2 create-internet-gateway --region $AWS_REGION --query 'InternetGateway.InternetGatewayId' --output text)
echo "Internet Gateway created with ID: $IGW_ID"

# Attach Internet Gateway to VPC
aws ec2 attach-internet-gateway --vpc-id $VPC_ID --internet-gateway-id $IGW_ID --region $AWS_REGION
echo "Internet Gateway attached to VPC."

# Create EC2 instance (example)
echo "Launching EC2 instance..."
INSTANCE_ID=$(aws ec2 run-instances --image-id ami-0c55b159cbfafe1f0 --instance-type t2.micro --subnet-id $SUBNET_ID --query 'Instances[0].InstanceId' --output text)
echo "EC2 instance launched with ID: $INSTANCE_ID"

# Output VPC, Subnet, and Instance IDs
echo "VPC ID: $VPC_ID"
echo "Subnet ID: $SUBNET_ID"
echo "EC2 Instance ID: $INSTANCE_ID"

echo "AWS resources setup complete."
