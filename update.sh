#!/bin/bash
sleep 1
sudo git reset --hard
sudo git pull https://github.com/85mattia/hello-world.git
echo UPDATE SUCCESSFUL
sleep 1
sudo chmod -R 777 ~
sleep 1
echo REBOOT
reboot
