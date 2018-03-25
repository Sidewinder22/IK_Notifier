#!/usr/bin/bash

if [ -z $2 ]
then
    echo -e "Not enough arguments!"
    echo -e "Using: \n\t$ ./run.sh -a login_param=[USER] -a password_param=[PASSWORD]"
    exit 1
fi

echo -e "########### {\_Sidewinder22_/} ############"
echo -e "IK_Spider\n"

scrapy runspider src/scraper.py -a login_param=$1 -a password_param=$2 

echo -e "\n########### {\_Sidewinder22_/} ###########"
echo -e "Bye..."
