import time

res = 1000  #重复次数
r = range(r)

def timer(func, *pargs, **kargs):
    start = time.clock()
    for i in r:
        ret = fun(*pargs, **kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)
    
