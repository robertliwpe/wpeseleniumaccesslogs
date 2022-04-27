#!/bin/bash

printf "\r\n\r\n=====================================================================================\r\n\r\n"
printf '\e[1;34m%-6s\e[m' "WP Engine User Portal Access Logs Automator"
printf "\r\n\r\n=====================================================================================\r\n\r\n"
printf "This will deploy a python script to download Complete Access Logs (within last 2 calendar days) from chosen installs\r\nDependencies: python3 pip selenium chromedriver\r\n\r\n"

if [ ! -f "./globalvars.txt" ];
then
    touch globalvars.txt
    read -r -p "Add your username: " username
    echo "# Username" >> ./globalvars.txt 
    echo "$username" >> ./globalvars.txt 

    stty -echo
    read -r -p "Add your password: " password
    printf "Password accepted...\r\n"
    stty echo
    echo "# Password" >> ./globalvars.txt 
    echo "$password" >> ./globalvars.txt 
else
    printf "Username Password found in globalvars.txt\r\n"
fi;

if [ ! -f "./installlist.txt" ];
then
    touch installlist.txt
    printf "What are the installs we are pulling Access Logs for?\r\n(if pasting multiple use a SPACE separator)\r\n"
    read -r accessloglist
    echo "# Installs" >> ./installlist.txt
    echo -n "$accessloglist" >> ./installlist.txt
else
    printf "Install List found in installlist.txt\r\n"
fi;

printf "\r\nExecuting Access Log Download script now...\r\n\r\n"

python3 ./accesslogpullv1.py

printf "\r\nDownload Operation COMPLETE! Feel free to close the open Chrome Browser...\r\n"
sleep 2
printf "Initiating cleanup...\r\n"

printf "\r\nWould you like to cache your username password combination (NOT RECOMMENDED)? (y/n)\r\n"
read -r unamecache

if [ "$unamecache" != "${unamecache#[Yy]}" ] ;
then 
    printf "Username Password combination kept in globalvars.txt\r\n"
else
    printf "Removing...\r\n"
    rm ./globalvars.txt
fi;

printf "\r\nWould you like to cache your install list? (y/n)\r\n"
read -r installcache

if [ "$installcache" != "${installcache#[Yy]}" ] ;
then 
    printf "Installs cached in installist.txt\r\n"
else
    printf "Removing...\r\n"
    rm ./installlist.txt
fi;