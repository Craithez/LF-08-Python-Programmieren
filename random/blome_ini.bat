:: blome.ini Aktualisierung 
:: Marc Lo Verde - LAV - 24.10.24
:: Frägt Laufwerknamen ab und legt eine Variable an.
@echo off
set /p AUSGANGSLAUFWERK=Datenort/USB Laufwerk angeben:
:while
::Frägt den Benutzernamen ab und legt eine Variable an.
set /p EINGABE=Benutzernamen eingeben: 
md C:\Users\%EINGABE%\AppData\Local\VirtualStore\Windows
copy "D:\Installation LIMS\blome.ini" "C:\Users\%EINGABE%\AppData\Local\VirtualStore\Windows
copy "D:\Installation LIMS\blome.ini" "C:\Windows\"
explorer C:\Users\%EINGABE%\AppData\Local\VirtualStore\Windows

set /p FORTSETZEN=Moechten Sie weitere Verzeichnisse kopieren? (j/n): 
if /i "%FORTSETZEN%"=="j" (
  echo %FORTSETZEN%
  goto :while
) else (
  echo Die Aktualisierung ist abgeschlossen.
  pause
  echo Aktualisierung der GPO
  gpupdate /force
)