echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 37PCL046 53913 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 32012) 
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 43216) 
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 30880)
del "C:\Users\y.chavali.176\OneDrive - Cranfield University\fm_assignment\ICEM\cleanup-fluent-37PCL046-43216.bat"
