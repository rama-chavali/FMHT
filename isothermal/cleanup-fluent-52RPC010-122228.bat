echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 52RPC010 55343 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="52RPC010" (%KILL_CMD% 147700) 
if /i "%LOCALHOST%"=="52RPC010" (%KILL_CMD% 155908) 
if /i "%LOCALHOST%"=="52RPC010" (%KILL_CMD% 133324) 
if /i "%LOCALHOST%"=="52RPC010" (%KILL_CMD% 153604) 
if /i "%LOCALHOST%"=="52RPC010" (%KILL_CMD% 122228) 
if /i "%LOCALHOST%"=="52RPC010" (%KILL_CMD% 152912)
del "C:\Users\Y.Chavali.176\OneDrive - Cranfield University\fmht\isothermal\cleanup-fluent-52RPC010-122228.bat"
