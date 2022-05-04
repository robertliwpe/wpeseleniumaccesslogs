#!/bin/bash

printf "\r\n=====================================================================================\r\n\r\n"
printf '\e[1;34m%-6s\e[m' "WP Engine User Portal Access Logs Automator"
printf "\r\n\r\n=====================================================================================\r\n\r\n"
printf "This will deploy a python script to download Complete Access Logs (within last 2 calendar days) from chosen installs\r\nThis script does not work with customer MFA or SSO. It is recommended you create a dedicated user account in the User Portal with the minimum access required for this script. Ensure that all files are kept within the same directory.\r\nDependencies: python3 pip selenium chromedriver\r\n\r\n"
printf "NOTE: Pendo notification popups in the User Portal WILL DISRUPT THIS SCRIPT. If Any unexpected notifications or popups do occur, rerun this script.\r\n\r\n"

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

    read -r -p "Do you want default \"Y\" responses to prompts? (y/n) (Select Y if you plan on running this unattended) " defaultresp
    echo "# Default Response Value" >> ./globalvars.txt 
    echo "$defaultresp" >> ./globalvars.txt 
else
    printf "Username Password & Defaults found in globalvars.txt\r\nDecrypting...\r\n"
    python3 ./decry.py
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

printf "\r\nMoving Logs to $PWD/logs...\r\n"

mkdir -p ./logs
mv ./*.csv ./logs

printf "\r\nDownload Operation COMPLETE! Feel free to close the open Chrome Browser...\r\n"
sleep 2
printf "Initiating cleanup...\r\n"
printf "Timeouts to all prompts from this point are 3 SECONDS...\r\n"

defaultrepout=$(cat ./globalvars.txt | tail -1)

printf '%s' "Current default response to prompts is: $defaultrepout"

TMOUT=3
printf "\r\n\r\nWould you like to cache your username password combination (NOT RECOMMENDED)? (y/n)\r\n"
read -r unamecache
unamecache=${unamecache:-$defaultrepout}

if [ "$unamecache" != "${unamecache#[Yy]}" ] ;
then
    if [[ -f filekey.key ]]
    then
        printf "Encryption Key found\r\nEncrypting Username Password...\r\n"
        python3 ./enc.py
    else
        printf "Encryption Key NOT found\r\nCreating...\r\n"
        python3 ./gen.py
        printf "Encryption Key CREATED! Do NOT delete otherwise your Username and Password will be lost forever\r\nCommencing Encryption...\r\n"
        python3 ./enc.py
    fi
    printf "Username Password combination kept in globalvars.txt\r\n"
else
    printf "Removing...\r\n"
    rm ./globalvars.txt
fi;

TMOUT=3
printf "\r\nWould you like to cache your install list? (y/n)\r\n"
read -r installcache
installcache=${installcache:-$defaultrepout}

if [ "$installcache" != "${installcache#[Yy]}" ] ;
then
    printf "Installs cached in installist.txt\r\n"
else
    printf "Removing...\r\n"
    rm ./installlist.txt
fi;

printf "\r\n"
TMOUT=0