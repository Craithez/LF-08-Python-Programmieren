@echo off
:: rem 3,2 für dd/mm/yyyy
set month-num=%date:~3,2%
if %month-num%==01 set mo-name=01 - Januar
if %month-num%==02 set mo-name=02 - Februar
if %month-num%==03 set mo-name=03 - März
if %month-num%==04 set mo-name=04 - April
if %month-num%==05 set mo-name=05 - Mai
if %month-num%==06 set mo-name=06 - Juni
if %month-num%==07 set mo-name=07 - Juli
if %month-num%==08 set mo-name=08 - August
if %month-num%==09 set mo-name=09 - September
if %month-num%==10 set mo-name=10 - Oktober
if %month-num%==11 set mo-name=11 - November
if %month-num%==12 set mo-name=12 - Dezember
:: Ein Array wäre eleganter, aber dann wäre ich kein FISI.

:: Pfade setzen und die Datei kopieren
set source="C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\MySirius.bak"
:: set ziel="X:\Zielordner"
set ziel="C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\Backup\%mo-name%\MySirius_Sicherung_%date%.bak"

@copy %source% %ziel%