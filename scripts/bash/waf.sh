#!/bin/bash

aws wafv2 create-web-acl --name "MyWAF" --scope "REGIONAL" --default-action Allow={} --rules "[{...}]"
