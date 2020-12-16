@echo off
:Main
echo.
echo.
echo Nitrotype auto typer
echo.
echo.
echo 1} Type on your account (~100 wpm)
echo.
echo 2} Type as guest (~100 wpm)
echo 3} Instant type as guest! (4,000-10,000 wpm)
echo.
echo (Press 1, 2, or 3)
set /p select=
if %select% EQU 1 goto Bot 
if %select% EQU 2 goto BotGuest
if %select% EQU 3 goto BotGuestInstant
:Bot
cls
echo starting...
cls
python bot.py
exit
:BotGuest
cls
echo starting...
python botguest.py
exit
:BotGuestInstant
cls
echo starting...
python botguestinstant.py
exit