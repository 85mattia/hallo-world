#!/bin/bash
sleep 1
sudo git reset --hard
sudo git pull https://github.com/85mattia/hello-world.git
echo UPDATE SUCCESSFUL
sudo chmod -R 777 ~
echo REBOOT
sleep 2
reboot
