@echo off

title Installing Pre-requsites
type requirements.txt
echo:

set /p yn="Do you want to proceed? [Y/n] "

if /i "%yn%"=="y" goto install
if /i "%yn%"=="yes" goto install
if /i "%yn%"=="n" goto exit
if /i "%yn%"=="no" goto exit
echo invalid response
goto end

:install
echo installing...
start pip install -r requirements.txt
goto end

:exit
echo exiting...
exit

:end