#!/usr/bin/env bash


sudo gpio mode 7 out
sudo gpio write 7 1
sleep 1
sudo gpio write 7 0

