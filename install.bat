@echo off 

cd py
if %PROCESSOR_ARCHITECTURE%==x86 (msiexec /i python-2.7.8.msi)else (msiexec /i python-2.7.8.amd64.msi)
cd ..
