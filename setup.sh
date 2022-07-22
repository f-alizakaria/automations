#!/bin/bash

if [ `find /home/"$1" -name Bureau` ]; then
  desktopDir=`find /home/"$1" -name Bureau`
elif [ `find /home/"$1" -name Desktop` ]; then
  desktopDir=`find /home/"$1" -name Desktop`
fi


if [ -z "$1" ] # if no parameter
  then
    echo "\nVeuillez respecter la synthaxe:\n\tsh ./setup.sh <profile_name>\n"
    exit
  else
    sudo python3 ./setup.py "$1" "$2" # username url
    gio set "$desktopDir"/handddle.desktop metadata::trusted true
    gio set "$desktopDir"/maintenance.desktop metadata::trusted true
    echo "\nConfiguration terminée !\n"
fi
