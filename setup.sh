#!/bin/bash


if [ $(whoami) = "root" ]; then
  # shellcheck disable=SC2028
  echo "\nN'exécutez pas ce scrit en tant que root !\n"
  exit
fi

if [ `find /home/"$1" -name Bureau` ]; then
  desktopDir=`find /home/"$1" -name Bureau`
elif [ `find /home/"$1" -name Desktop` ]; then
  desktopDir=`find /home/"$1" -name Desktop`
fi


if [ -z "$1" ] # if no parameter
  then
    echo "\nVeuillez respecter la synthaxe:\n\tsh ./setup.sh <profile_name> <app_url>\n"
    exit
  else
    echo "\nLa cnfiguration ne prendra que quelques secondes.\nVeuillez patienter.\n"
    sudo python3 ./setup_complementary.py "$1" "$2" # username url
    gio set "$desktopDir"/handddle.desktop metadata::trusted true
    gio set "$desktopDir"/maintenance.desktop metadata::trusted true
    echo "\nConfiguration terminée !\n"
fi