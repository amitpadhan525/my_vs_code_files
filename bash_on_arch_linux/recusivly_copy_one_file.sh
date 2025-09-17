read -p "Enter source file path : " source
read -p "Enter destination path : " destination
read -p "How many times copy : " number


filename=$(basename $source)
name="${filename%.*}"
ext="${filename##*.}"

# echo $name
# echo $ext
for ((i=1;i<=number;i++)); do
    cp "$source" "$destination/${name}$i.${ext}"
done