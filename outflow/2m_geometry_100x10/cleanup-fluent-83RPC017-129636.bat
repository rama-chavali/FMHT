echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 83RPC017 52909 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 139628) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 121580) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 135296) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 132468) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 129636) 
if /i "%LOCALHOST%"=="83RPC017" (%KILL_CMD% 139368)
del "C:\Users\y.chavali.176\OneDrive - Cranfield University\fm_assignment\outflow\2m_geometry_100x10\cleanup-fluent-83RPC017-129636.bat"
