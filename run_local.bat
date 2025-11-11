@echo off
REM =========================================================================
REM Script to run Django server with LOCAL settings (SQLite + Local Storage)
REM =========================================================================

echo.
echo ============================================================
echo Starting Django Server with LOCAL settings
echo ============================================================
echo.
echo Database: SQLite (db.sqlite3)
echo Static Files: Local (staticfiles/)
echo Media Files: Local (media/)
echo.
echo ============================================================
echo.

set DJANGO_SETTINGS_MODULE=config.settings_local
env\Scripts\python.exe manage.py runserver

pause
