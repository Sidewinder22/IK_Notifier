#!/bin/bash

if [ -z $2 ]
then
    echo -e "Not enough arguments!"
    echo -e "Using: \n\t$ ./run.sh [USER] \"[PASSWORD]\""
    exit 1
fi

echo -e "########### {\_Sidewinder22_/} ############"
echo -e "IK_Spider is working..."

while true;
    do
    scrapy runspider src/spider.py -a login_param=$1 -a password_param=$2 --nolog
    #sleep 300
    sleep 10
done

echo -e "\n########### {\_Sidewinder22_/} ###########"
echo -e "Bye..."
