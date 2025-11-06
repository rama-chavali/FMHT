echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 83RPC017 51090 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 124128) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 118496) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 131932) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 117448) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 136344) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 121252)
del "C:\Users\y.chavali.176\OneDrive - Cranfield University\fm_assignment\pressure_outlet\coarse10mpressureoutlet\cleanup-fluent-83RPC017-136344.bat"
