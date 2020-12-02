#!/bin/bash

if [[ $(pip3 freeze | grep configargparse) ]]
then
	echo "installed"
else
	pip3 install configargparse
fi
