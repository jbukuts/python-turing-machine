#!/bin/bash

if [[ $(pip3 freeze | grep -i configargparse) ]]
then
	echo "configargparse already installed. skipping."
else
	pip3 install configargparse
fi
