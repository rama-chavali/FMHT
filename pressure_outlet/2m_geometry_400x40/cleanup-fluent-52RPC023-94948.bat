echo off
set LOCALHOST=%COMPUTERNAME%
set KILL_CMD="C:\PROGRA~1\ANSYSI~1\v252\fluent/ntbin/win64/winkill.exe"

start "tell.exe" /B "C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\tell.exe" 52RPC023 52131 CLEANUP_EXITING
timeout /t 1
"C:\PROGRA~1\ANSYSI~1\v252\fluent\ntbin\win64\kill.exe" tell.exe
if /i "%LOCALHOST%"=="52RPC023" (%KILL_CMD% 140220) 
if /i "%LOCALHOST%"=="52RPC023" (%KILL_CMD% 94948) 
if /i "%LOCALHOST%"=="52RPC023" (%KILL_CMD% 125272)
del "C:\Users\Y.Chavali.176\OneDrive - Cranfield University\fmht\pressure_outlet\2m_geometry_400x40\cleanup-fluent-52RPC023-94948.bat"
