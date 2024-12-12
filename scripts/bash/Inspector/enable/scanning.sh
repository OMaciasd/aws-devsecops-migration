#!/bin/bash

aws inspector2 enable
aws inspector2 create-findings-report \
    --filter '{ "resourceType": ["EC2Instance"], "severities": ["CRITICAL"] }'
