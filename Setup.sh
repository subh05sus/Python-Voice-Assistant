#!/bin/sh

echo "These following packages would be installed.."
echo "why"
echo "customtkinter"
echo "pyttsx3"
echo "datetime"
echo "speech_recognition"
echo "wikipedia"
echo "pyautogui"
echo "screen_brightness_control"
echo "pyscreenshot"
echo "bs4"
echo "requests"
echo "pyjokes"



read -p "Do you want to proceed? (yes/no) " yn

case $yn in 
	yes ) echo installing...;;
	no ) echo exiting...;
		exit;;
	* ) echo invalid response;
		exit 1;;
esac

pip install why
pip install customtkinter
pip install pyttsx3
pip install datetime
pip install speechrecognition
pip install wikipedia
pip install pyautogui
pip install screen_brightness_control
pip install pyscreenshot
pip install bs4
pip install requests
pip install pyjokes
pip install openai
