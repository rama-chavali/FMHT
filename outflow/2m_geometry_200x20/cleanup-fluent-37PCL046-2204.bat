echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 37PCL046 55844 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 23248) 
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 2204) 
if /i "%LOCALHOST%"=="37PCL046" (%KILL_CMD% 18760)
del "C:\Users\y.chavali.176\OneDrive - Cranfield University\fm_assignment\2m_geometry_200x20\cleanup-fluent-37PCL046-2204.bat"
