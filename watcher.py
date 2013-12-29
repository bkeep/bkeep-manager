# -*- coding: utf-8 -*-
import logging
import time,socket,sys
from kazoo.client import KazooClient,KazooState
import subprocess as sb

#logging.basicConfig(level=logging.DEBUG)
logging.basicConfig(level=logging.ERROR)

zk = KazooClient("1.24.79.51:2181,1.24.79.53:2181",timeout=500,max_retries=1)
zk.start()

def listener(state):
    if state == KazooState.LOST:
        print ">>>>listener saw KazooState.LOST"
        #zk.stop()
        zk.start()
    elif state == KazooState.SUSPENDED:
        print ">>>>listener saw KazooState.SUSPENDED"
    else:
        print ">>>>listener saw KazooState.CONNECTED"

class WatchData():
    def __init__(self,path):
        self.tmp = "/tmp/"
        if path:
            self.path = path
        else:
            self.path = "/bkeep/favorite/cmd"
        if zk.exists(self.path):
            print ("path:%s  exists " % (self.path)) 
        else:
            zk.ensure_path(self.path)
            zk.set(self.path, b"new create")

    def download(self,url):
        self.url = url
        self.cmd = "wget " + self.url + " -q -N -P " + self.tmp
        return_code = sb.call(self.cmd,shell = True)
        if return_code == 0:
            print ("download %s ok" % self.url)
        else:
            print ("download %s error!" % self.url)

    def str2list(self,s):
        self.s = s
        exec 'ss = %s' % self.s
        return ss

    def watchxxx(self):
        @zk.DataWatch(self.path)
        def Watch_cmd(data,stat):
            #json
            #[{ip:"",url:"",name:"",cmd:""}]
            s = self.str2list(data.decode("utf-8"))
            self.download(s[0]['url'])
            print s

class Monitor():
    def __init__(self):
        pass
    def gethostname(self):
        myname  = socket.getfqdn(socket.gethostname())
        return myname

    def getlocalip(self):
        self.myname  = socket.getfqdn(socket.gethostname())
        myip = socket.gethostbyname(self.myname)
        return  myip

    def getmem(self):
        mem = {}
        f = open("/proc/meminfo")
        lines = f.readlines()
        f.close()
        for line in lines:
            if len(line) < 2: continue
            name = line.split(':')[0]
            var = line.split(':')[1].split()[0]
            mem[name] = long(var) * 1024.0
        #mem['MemUsed'] = mem['MemTotal'] - mem['MemFree'] - mem['Buffers'] - mem['Cached']
        return mem['MemTotal']

    def getcpu(self):
        cpu = []
        cpuinfo = {}
        f = open("/proc/cpuinfo")
        lines = f.readlines()
        f.close()
        for line in lines:
            if line == '\n':
                cpu.append(cpuinfo)
                cpuinfo = {}
            if len(line) < 2: continue
            name = line.split(':')[0].rstrip()
            var = line.split(':')[1]
            cpuinfo[name] = var
        cpucount = int(cpu[-1]['processor']) + 1
        cpuinfo = []
        cpuinfo.append({"model name":cpu[-1]["model name"],"cpucount":cpucount})
        #[{'cpucount': 24, 'model name': ' Intel(R) Xeon(R) CPU E5-2630 0 @ 2.30GHz\n'}]
        return cpuinfo

    def getconf(self):
        pass
    def hearbeat(self):
        pass

class SetData():
    def setdata(self,path,data):
        self.path = path
        self.data = data
        zk.set(self.path,self.data)

if __name__ == "__main__":
    #create connect
    zk.add_listener(listener)
    
    # watch node data
    wd = WatchData("")
    wd.watchxxx()

    # monitor
    mn = Monitor()
    print mn.gethostname()
    print mn.getlocalip()
    print mn.getmem()
    print mn.getcpu()

    # set data
    sd = SetData()
    #sd.setdata("","")
    time.sleep(1000)
  
