@echo off
REM echo One moment, loading..
REM Loading DLL's
REM TODO: Find out if all these actually are neccesary
REM TODO: Make the python script handle this.
REM regsvr32 /s dispex.dll
REM regsvr32 /s jscript.dll
REM regsvr32 /s scrrun.dll
REM regsvr32 /s vbscript.dll
REM regsvr32 /s wshext.dll
REM regsvr32 /s wshom.ocx
REM wpeinit

REM echo.
REM echo Done, running user interface:
REM X:
cd X:\GUI
REM Hiding the annoying black box in PE
REM See LICENSE for information about cmdow
cmdow @ /hid
TITLE Installer running..
X:\PortablePython\App\python.exe X:\__init__.py
REM We arent actually suppoused to get this far, WDP will shutdown
exit