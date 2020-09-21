#!/bin/bash
cd /home/rf/FTP
OF=$(date "+%Y%m%d")
mkdir backup/$OF

mv *$OF* /home/rf/FTP/backup/$OF/
