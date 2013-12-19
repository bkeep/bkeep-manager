# -*- coding: utf-8 -*-
import logging
import time,socket
from kazoo.client import KazooClient,KazooState

logging.basicConfig(level=logging.DEBUG)

zk = KazooClient("x.24.79.51:2181,x.24.79.53:2181",timeout=500,max_retries=1)
zk.start()

def listener(state):
    if state == KazooState.LOST:
        print ">>>>listener saw KazooState.LOST"
        #zk.stop()
        #zk.start()
    elif state == KazooState.SUSPENDED:
        print ">>>>listener saw KazooState.SUSPENDED"
    else:
        print ">>>>listener saw KazooState.CONNECTED"
zk.add_listener(listener)
print "------sleeping"
time.sleep(1000)
