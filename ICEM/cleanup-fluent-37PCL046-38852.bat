echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 37PCL046 51657 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 31772) 
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 38852) 
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 30484)
del "C:\Users\y.chavali.176\ICEM\cleanup-fluent-37PCL046-38852.bat"
