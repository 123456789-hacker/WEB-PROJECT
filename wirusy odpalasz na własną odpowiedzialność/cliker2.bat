@echo off
title cliker
color f
mode 30,5
set x=0
:menu
echo klikniecia: %x%
call 1.vbs
set /a x+=1
goto menu