read -p "Enter path " path


for file in $path/*.txt;
do
    echo $file
done