# -*- coding: utf-8 -*-
import time,socket,sys
from kazoo.client import KazooClient,KazooState
import logging
logging.basicConfig(level=logging.DEBUG)

class dzk:
    def __init__(self):
        self.BasePath = "/my/"
        self.zk = KazooClient(hosts='x.24.79.51:2181,x.24.79.53:2181',retry_max_delay=2000)
        self.zk.start()
        self.zk.add_listener(self.listener)

    def listener(state):
        if state == KazooState.LOST:
            self.zk.start()
        elif state == KazooState.SUSPENDED:
            print "*******listener saw KazooState.LOST"
        else:
            print "*******listener saw KazooState.CONNECT"

    def getIpHost(self):
        self.myname  = socket.getfqdn(socket.gethostname())
        myip = socket.gethostbyname(self.myname)
        return  myip

    def register(self):
        ip = self.getIpHost()
        if ip:
            NODE = self.BasePath + ip
            print "register:",NODE
        else:
            print "[ERROR:] %s does not exist " %(NODE)
            sys.exit(2)

        if not self.zk.exists(NODE): 
            self.zk.ensure_path(NODE)

    def getData(self):
        ip = self.getIpHost()
        if ip:
            NODE = self.BasePath + ip
        else:
            print "[ERROR:] %s does not exist " %(NODE) 

        if self.zk.exists(NODE):
            data, stat = self.zk.get(NODE)
            print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

    def monitor(self):
        pass
    
    def heartbeat(self):
        pass

    def role(self):
        pass
    
    def command(self):
        pass

        
if __name__ == "__main__":
    czk = dzk()
    while 1:
        czk.register()
        time.sleep(10)
        czk.getData()
