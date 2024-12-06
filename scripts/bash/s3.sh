#!/bin/bash

aws cloudformation create-stack --stack-name MyCodePipelineStack --template-body file://codepipeline.yaml
