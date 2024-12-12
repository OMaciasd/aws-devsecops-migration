#!/bin/bash

aws guardduty enable
aws guardduty get-findings --detector-id <detector-id>
