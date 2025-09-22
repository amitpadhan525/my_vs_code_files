read n
result=0
for ((i=1;i<=n;i++));do
    result=result+n
done

echo $((result/n))