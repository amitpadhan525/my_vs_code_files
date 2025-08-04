read -p "Enter a number :" a
read -p "Enter another number :" b
if [ $a -eq $b ];then
    echo "Both Number Same"
elif [ $a -lt $b ];then
    echo "$a less then $b"
elif [ $a -gt $b ];then
    echo "$a grater then $b"
else
    echo "error"
fi