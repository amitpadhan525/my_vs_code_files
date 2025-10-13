path=/home/spider/amit.txt

filename=$(basename $path)
filename1="${path##*/}"     #remove everythink before last /
filename_without_extension="${filename1%.*}"        #remove everythink after .
extension="${path##*.}"



echo $filename
echo $filename1
echo $filename_without_extension
echo $extension