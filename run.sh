#!/usr/bin/bash

if [ -z $2 ]
then
    echo -e "Not enough arguments!"
<<<<<<< HEAD
    echo -e "Using: \n\t$ ./run.sh -a login_param=[USER] -a password_param=[PASSWORD]"
=======
    echo -e "Using: \n\t$ ./run.sh [USER] [PASSWORD]"
>>>>>>> 7c4eb956d69fb76b47512523c272e557b9e55ce0
    exit 1
fi

echo -e "########### {\_Sidewinder22_/} ############"
echo -e "IK_Spider\n"

scrapy runspider src/scraper.py -a login_param=$1 -a password_param=$2 

echo -e "\n########### {\_Sidewinder22_/} ###########"
echo -e "Bye..."
