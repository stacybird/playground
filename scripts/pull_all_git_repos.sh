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

cd $1
for i in $(ls); do
    cd $i
    printf "\n"$i"\n"
    git checkout master |grep -v up-to-date
    git pull --ff-only |grep -v Already|grep -v Current
    cd ../
done
