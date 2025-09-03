#!/bin/bash
cd /home/amit/Desktop/my_vs_code_files || exit
git add .
git commit -m "Auto update on $(date '+%Y-%m-%d %H:%M:%S')"
git push origin master
