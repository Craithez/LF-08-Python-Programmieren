:: QGIS PostgreSQL Database Backup
:: MLV - 16.09.2024
:: für LAV und LVGL
@echo Backup Database  %PG_PATH%%PG_FILENAME%
@echo off
SET PG_BIN="C:\Program Files\PostgreSQL\16\bin\pg_dump.exe"
:: Alternativ "\bin\pg_dump.exe" in einem extra Ordner.
SET PG_HOST=localhost
SET PG_PORT=5432
:: Es muss ein neuer Benutzer angelegt werden, root funktioniert nicht.
SET PG_DATABASE=DATENBANKNAME
SET PG_USER=BENUTZER
SET PG_PASSWORD=PASSWORT
SET PG_PATH=C:\Pfad


SET PG_FILENAME=%PG_PATH%\%PG_DATABASE%_%date%.sql

%PG_BIN% -h %PG_HOST% -p %PG_PORT% -U %PG_USER% %PG_DATABASE% > %PG_FILENAME%
pause
@echo Backup wurde erfolgreich gesichert! -> %PG_PATH%%PG_FILENAME%