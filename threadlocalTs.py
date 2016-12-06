#coding:utf-8
"""
Date:2016/12/06
Author:Hyman
"""
import threading
localobj=threading.local()

def thread_func(name):
    """
    线程函数
    Example:
    >>> import threading
    >>> t=threading.Thread(target=thread_func,args=('Hyman',))
    """
    localobj.name=name
    print 'localobje.name=%s'%localobj.name

if __name__=='__main__':
    t1=threading.Thread(target=thread_func,args=('Hyman',))
    t2=threading.Thread(target=thread_func,args=('Liuzhihui',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
