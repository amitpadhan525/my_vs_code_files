#!/bin/bash
# THIS FILE ONLY FOR PUSH FILES AND FOLDER TO GITHUB

read -p "Enter commit message: " commit
git add .
git commit -m "$commit"
git push origin main
