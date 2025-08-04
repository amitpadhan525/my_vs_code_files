#!/bin/bash
cd ~/my_vs_code_files

git add .
git commit -m "auto update on $(date '+%Y-%m-%d %H:%M:%S')"
git push origin master
