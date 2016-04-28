#使用类装饰器来追踪调用
#不支持类方法
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func
    # **kwargs用于支持关键字参数
    def __call__(self, *args, **kwargs):
        self.calls += 1
        print('call %s to %s'%(self.calls, self.func.__name__))
        self.func(*args, **kwargs)

#把spam变成tracer的一个实例，spam原来的方法变成了这个实例的self.func
#每当调用spam时，即调用这个实例的__call__方法。
@tracer
def spam(a, b, c):
    print(a + b + c)

@tracer
def a(a,b):
    print(a+b)
    
if __name__ == '__main__':
    spam(1,2,3)
    a(2,3)
    spam(2,3,4)
    a(4,5)
    spam

print('使用函数装饰器来实现相同的功能')
print('而且支持类方法')
def tracer(func):
    calls = 0
    def wrapper(*arg, **kwargs):
        nonlocal calls
        calls += 1
        print('call %s to %s'%(calls, func.__name__))
        return func(*arg, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):
    print(a + b + c)

@tracer
def a(a,b):
    print(a+b)
    
if __name__ == '__main__':
    spam(1,2,3)
    a(2,3)
    spam(2,3,4)
    a(4,5)
    spam