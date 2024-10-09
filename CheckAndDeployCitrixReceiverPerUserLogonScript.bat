
set DesiredVersion=12.03.05

set DeployDirectory=\\10.8.168.34\test

set logshare=\\10.8.168.34\test\

set CommandLineOptions=/silent SERVER_LOCATION="BVVNinstsrvr22.ftltest.eng.citrite.net" ENABLE_SSON="Yes"


echo %date% %time% the %0 script is running >> %logshare%%ComputerName%.log


IF NOT "%ProgramFiles(x86)%"=="" SET WOW6432NODE=WOW6432NODE\

REM
reg query "HKEY_CURRENT_USER\SOFTWARE\%WOW6432NODE%Citrix\PluginPackages\XenAppSuite\ICA_Client" | findstr %DesiredVersion%
if %errorlevel%==1 (goto NotFound) else (goto Found)
REM

:NotFound
start /wait %DeployDirectory%\CitrixWorkspaceApp.exe /SILENT
REM
echo %date% %time% Setup ended with error code %errorlevel%. >> %logshare%%ComputerName%.log
type %temp%\TrolleyExpress*.log >> %logshare%%ComputerName%.log

goto End

:Found
echo %date% %time% Package was detected, Halting >> %logshare%%ComputerName%.log
goto End


:End
echo %date% %time% the %0 script has completed successfully >> %logshare%%ComputerName%.log
Endlocal
