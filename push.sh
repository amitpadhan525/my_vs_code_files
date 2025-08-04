
# THIS FILE ONLY FOR PUSH FILES AND FOLDER TO GITHUB

git add .
read -p "Enter commit for changes :" msg
git commit -m "$msg $(date '+%Y-%m-%d %H:%M:%S')"
git push


