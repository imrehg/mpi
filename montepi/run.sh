#!/bin/bash

if [ -z "$1" ]
then
    PROCESSORS=2
else
    PROCESSORS=$1
fi
mpiexec -n $PROCESSORS python montepi.py
