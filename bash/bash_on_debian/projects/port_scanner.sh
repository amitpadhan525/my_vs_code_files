#!/bin/bash
read -p "Enter taget IP address :" ip
read -p "Enter port no. :" port
nmap $port $ip