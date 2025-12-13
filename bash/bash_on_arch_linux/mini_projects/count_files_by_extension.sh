#!/bin/bash
path=/home/spider/my_vs_code_files

for file in "$path"/*; do
    if [ -f "$file" ] && [[ "$file" == *.* ]]; then
        ext="${file##*.}"
        echo "$ext"
    fi
done | sort | uniq -c | sort -nr
