#!/bin/bash

aws securityhub get-findings --filters '{"SeverityLabel": [{"Value": "HIGH", "Comparison": "EQUALS"}]}' > security-findings.json
