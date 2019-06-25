#!/bin/bash

if [ -z "$1" ]; then 
    echo usage: $0 directory
    exit
fi

STR=`which git`
if [ "$STR" == "" ]; then
    echo "Sorry, git needs to be installed first"
    exit
fi

ssh-add -l > /dev/null 2>&1
if [ $? == 1 ]; then
    echo "Please ssh-add your key before pulling repos in an automated fashion"
    exit
fi

PWD=`pwd`
for i in $( find $1 -name ".git" | sort | sed 's/....$//' ); do
    cd $i
    printf "\n"$i"\n"
    git checkout master |grep -v up-to-date
    git pull --ff-only |grep -v Already|grep -v Current
done
cd $PWD

