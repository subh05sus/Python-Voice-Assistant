#!/bin/bash

cat requirements.txt

echo
read -p "Do you want to proceed? [Y/n] " yn

case $yn in 
	y ) echo installing...;;
	yes ) echo installing...;;
	n ) echo exiting...;
		exit;;
	no ) echo exiting...;
		exit;;
	* ) echo invalid response;
		exit 1;;
esac

pip install -r requirements.txt or pip3 install -r requirements.txt
sudo apt-get install libasound-dev