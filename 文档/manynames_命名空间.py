#模块属性/全局变量
X = 11

def f():
    print(X)

#函数内的本地变量
def g():
    X = 22
    print(X)

class C:
    #类属性
    X = 33
    def m(self):
        #类方法中的本地变量
        X = 44
        #实例属性
        self.X = 55
        
if __name__ == '__main__':
    print(X)        #11:模块变量
    f()                #11:全局变量
    g()               #22:本地变量
    print(X)        #11:模块变量不会变
    
    obj = C()      #创建实例
    print(obj.X)  #33:类变量
    obj.m()        #把变量名X变成实例属性
    print(obj.X)  #55:实例属性
    print(C.X)     #33:类属性不变

    try:
        print(C.m.X)
    except:
        print('False: print(C.m.X)')
    try:
        print(g.X)
    except:
        print('False: print(g.X)')
