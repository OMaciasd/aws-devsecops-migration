#!/bin/bash

aws codeguru-reviewer create-code-review \
    --name lab-review \
    --repository-association-arn arn:aws:codecommit:<region>:<account-id>:lab-repo
