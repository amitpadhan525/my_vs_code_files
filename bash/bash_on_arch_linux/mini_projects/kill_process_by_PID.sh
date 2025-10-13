ps -e -o pid,comm --sort=pid

read -p "Enter PID which have to kill :" pid

kill $pid