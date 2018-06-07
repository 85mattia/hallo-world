#!/bin/bash
sleep 1
mkdir -p ../backup-timeatt
rm -rf ../backup-timeatt/*
cp -r . ../backup-timeatt
git reset --hard
git pull https://github.com/85mattia/hello-world.git
echo UPDATE SUCCESSFUL
sleep 1

