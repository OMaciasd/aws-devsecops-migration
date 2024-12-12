#!/bin/bash

aws cloudtrail create-trail --name lab-trail --s3-bucket-name lab-trail-logs
aws cloudwatch put-metric-alarm \
    --alarm-name HighCPUUtilization \
    --metric-name CPUUtilization \
    --namespace AWS/EC2 \
    --statistic Average \
    --period 300 \
    --threshold 80 \
    --comparison-operator GreaterThanThreshold \
    --dimensions Name=InstanceId,Value=<instance-id> \
    --evaluation-periods 2 \
    --alarm-actions <sns-topic-arn>
