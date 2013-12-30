#创建链接
from kazoo.client import KazooClient

zk = KazooClient(hosts='127.0.0.1:2181')
zk.start()

#创建链接并监控链接事件
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



# 如果路径不存在则自动创建
zk.ensure_path("/my/favorite")

# 创建一个带有数据的节点
zk.create("/my/favorite/node", b"a value")



# 如果节点存在
if zk.exists("/my/favorite"):
    # Do something

#读取节点数据
data, stat = zk.get("/my/favorite")
print("Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

# 打印子节点
children = zk.get_children("/my/favorite")
print("There are %s children with names %s" % (len(children), children))
 
#更新节点数据
zk.set("/my/favorite", b"some data")

#递归删除目录
zk.delete("/my/favorite/node", recursive=True)







