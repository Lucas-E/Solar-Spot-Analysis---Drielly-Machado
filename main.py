#---------------------------------------------------------------------------------------
#importing files
import config
import os
import platform 
import sys
from starModule import *
from configparser import ConfigParser
#---------------------------------------------------------------------------------------

#CONFIGURING CLEAR COMMAND
#----------------------------------------------------------------------------------------
configuration = ConfigParser()
configuration.read('config.ini')
CLEAR_COMMAND = configuration['CLEAR'][platform.system()]
#----------------------------------------------------------------------------------------


        
if __name__ == '__main__':
    os.system(CLEAR_COMMAND)
    menus.menuPrincipal()