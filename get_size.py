#cat get_size.py 
# -*- coding: utf-8 -*-
"""遍历指定路径下所有节点的大小"""
from kazoo.client import KazooClient,KazooState
import socket,sys, os, time, atexit

class dzk:
    def __init__(self,hosts,secs):
        self.hosts = hosts
        #self.zk = KazooClient(hosts='1.1.1.3:2181,1.1.1.2:2181,1.1.1.1:2181',retry_max_delay=2000)
        self.zk = KazooClient(hosts=self.hosts)
        try:
            self.zk.start()
            self.zk.add_listener(self.listener)
        except Exception,e:
            print "ERROR connect LOST ==============>"

    def listener(state):
        if state == KazooState.LOST:
            self.zk.start()
        elif state == KazooState.SUSPENDED:
            print "*******listener saw KazooState.LOST"
        else:
            print "*******listener saw KazooState.CONNECT"

    def get_child(self,paths):
        aa = self.zk.get_children(paths)
        return aa

    def getData(self,paths):
        xx = self.zk.get(paths)
        return xx[1][8]

    def bianli(self,rootDir):
        for i in self.get_child(rootDir):
            if i:
                i = rootDir + "/" + i
                #if self.getData(i) > 1048570:
                print i,"---->",self.getData(i)
                self.bianli(i)

if __name__ == "__main__":
    zzk = dzk("1.1.1.1:2181",2000)

    #zzk.get_child()
    #zzk.getData()
    zzk.bianli("/")
