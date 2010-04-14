import ConfigParser
import imp
import os
import sys

import windistp

# Reading the configuration from file
CONFIG = ConfigParser.RawConfigParser()
CONFIG.read('wdp.conf')

#TODO: check if user is using WindowsPE, else skip
#TODO: check what dlls are actually neccesary for operation
print "Activating network configuration.."
sys.path.insert(0, r'X:\Windows\System32') 
os.system("regsvr32 /s dispex.dll")
os.system("regsvr32 /s jscript.dll")
os.system("regsvr32 /s scrrun.dll")
os.system("regsvr32 /s vbscript.dll")
os.system("regsvr32 /s wshext.dll")
os.system("regsvr32 /s wshom.ocx")
os.system("wpeinit")
del sys.path[0] 

#TODO: Make the apps take values from config files
#Start WindistPoratable stage 1
APP = windistp.WindistPortable()
APP.mainWindow.mainloop()
# we are here assuming stage one has copied the rest of the instructions
# and resources, import stage 2 
SPCS2 = imp.load_source('windistp_s2', 'X:\windistp_s2.py')
# Start stage 2, remeber the user's language choice
APP = windispt_s2.SPCS2(APP.language)
# Give the new stage focus from the OS
APP.mainWindow.focus_force()
APP.mainWindow.mainloop()
