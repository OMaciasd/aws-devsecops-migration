#!/bin/bash

docker build -t vulnerable-image .
hub scan --image vulnerable-image
