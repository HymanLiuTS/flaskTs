#/usr/bin/env python
#coding:utf-8

from time import ctime,sleep

def settime(func):
    def tempfun(args):
        print '[%s] %s called'%(ctime(),func.__name__)
        print args
        return func
    return tempfun

@settime
def myfunc( arg ):
    pass

#调用一次myfunc(),sleep 4秒
myfunc("我是参数")
sleep(4)

#循环调用myfunc(),每次sleep 1秒
for i in range(2):
    myfunc("我是参数")
    sleep(1)
