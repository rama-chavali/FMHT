echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 37PCL035 59261 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="37PCL035" (%KILL_CMD% 18156) 
if /i "%LOCALHOST%"=="37PCL035" (%KILL_CMD% 50932) 
if /i "%LOCALHOST%"=="37PCL035" (%KILL_CMD% 29948) 
if /i "%LOCALHOST%"=="37PCL035" (%KILL_CMD% 30904) 
if /i "%LOCALHOST%"=="37PCL035" (%KILL_CMD% 18572) 
if /i "%LOCALHOST%"=="37PCL035" (%KILL_CMD% 29944)
del "C:\Users\y.chavali.176\OneDrive - Cranfield University\fm_assignment\2m_geometry_400x40\cleanup-fluent-37PCL035-18572.bat"
