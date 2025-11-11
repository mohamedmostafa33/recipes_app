@echo off
REM =========================================================================
REM Script to run Django server with AWS settings (PostgreSQL + S3)
REM =========================================================================

echo.
echo ============================================================
echo Starting Django Server with AWS settings
echo ============================================================
echo.
echo Database: PostgreSQL (AWS RDS)
echo Static Files: S3 (staticfiles/)
echo Media Files: S3 (media/)
echo.
echo ============================================================
echo.

set DJANGO_SETTINGS_MODULE=config.settings
env\Scripts\python.exe manage.py runserver

pause
