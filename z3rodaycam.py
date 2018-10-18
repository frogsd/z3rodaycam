#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import time
import random

# colour 
G = "\033[32m"; O = "\033[33m"; B = "\033[36m"; R = "\033[31m"; W = "\033[0m"; P = "\033[35m";

print O+("")
mess = """
        ____                _                             _             
     |___ \              | |                           | |            
  ____ __) |_ __ ___   __| | __ _ _   _   ___ _   _  __| | __ _ _ __  
 |_  /|__ <| '__/ _ \ / _` |/ _` | | | | / __| | | |/ _` |/ _` | '_ \ 
  / / ___) | | | (_) | (_| | (_| | |_| | \__ \ |_| | (_| | (_| | | | |
 /___|____/|_|  \___/ \__,_|\__,_|\__, | |___/\__,_|\__,_|\__,_|_| |_|
                                   __/ |                              
                                  |___/                               


                                                         """

print mess
print "                create  Z3roday Sudan"
print "                search pro plant shodan"
print "  Note :▂▃▄▅▆▇█▓▒░Now you can hacked fbi via Port 21 Anonymous░▒▓█▇▆▅▄▃▂"


def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.3)
mengetik('&_<︻╦̵̵͇̿̿̿̿ vist our site ╤───.......┣▇ https://zeroday-sudan.ml  ▇▇▇▇▇═─ ')

import shodan

SHODAN_API_KEY = "61rVASe34ZXkRIjW8wc6rWCJs6oVy4Kz"

api = shodan.Shodan(SHODAN_API_KEY)

try:

    #Search Shodan		
    results = api.search('linux+upnp+avtech')

    # Show the results
    print 'Results found: %s' % results['total']
    for result in results['matches']:
    		print 'IP: %s' % result['ip_str']
    		print result['data']
   		print ''
except shodan.APIError, e:
    print 'Error: %s' % e


