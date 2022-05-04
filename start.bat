@echo off & title TibiaAuto12 - Console

goto :DOES_PYTHON_EXIST

:DOES_PYTHON_EXIST
python -V | find /v "Python" >NUL 2>NUL && (goto :PYTHON_DOES_NOT_EXIST)
python -V | find "Python"    >NUL 2>NUL && (goto :PYTHON_DOES_EXIST)
goto :EOF

:PYTHON_DOES_NOT_EXIST
echo Python is not installed on your system.
echo Now opeing the download URL.
start "" "https://www.python.org/downloads/windows/"
pause
goto :EOF

:PYTHON_DOES_EXIST
python start.py
goto :EOF
