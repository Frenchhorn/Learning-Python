'''
装饰器其实也就是一个函数，一个用来包装函数的函数，返回一个修改之后的函数对象。经常被用于有切面需求的场景，较为经典的有插入日志、
性能测试、事务处理等。装饰器是解决这类问题的绝佳设计，有了装饰器，我们就可以抽离出大量函数中与函数功能本身无关的雷同代码并继续重用。概括的讲，装
饰器的作用就是为已经存在的对象添加额外的功能。
'''
首先来看看一个小例子：
def alan():
    print('alan speaking')

这是一个很简单的函数，就是输出“alan speaking”。
现在我再来改改这个函数，同时输出今天的时间：
def alan():
    print('alan speaking')
    date = datetime.utcnow()
    print(date)

这个时候，我有另外的函数，tom()、john()、Mary()也要输出类似句子。
怎么做？再写一个date在tom函数里？
为了减少重复写代码，我们可以这样做我重新定义一个函数：
def date(func):
    func()
    date = datetime.utcnow()
    print(date)
 
def alan():
    print('alan speaking')
 
def tom():
    print('tom speaking')
 
date(tom)

逻辑上不难理解，而且运行正常。
但是这样的话，我们每次都要将一个函数传递写入date中，如果我要实现直接调用alan()或者tom()就可以输出结果，又要避免重复写相同的代码，应该怎么修改？
def date(func):
    def wrapper():
        func()
        date = datetime.utcnow()
        print(date)
    return wrapper
 
def alan():
    print('alan speaking')
 
def tom():
    print('tom speaking')
 
tom = date(tom)
tom()

我们只需要在定义tom以后调用tom之前，加上tom= date(tom)，就可以达到目的。
这也就是装饰器的概念，看起来像是tom被date装饰了。
在在这个例子中，函数进入和退出时 ，被称为一个横切面(Aspect)，这种编程方式被称为面向切面的编程(Aspect-Oriented Programming)。

定义好装饰器后，我们就可以通过@语法使用了，使用装饰器输出我们想要的结果。
def date(func):
    def wrapper():
        func()
        date = datetime.utcnow()
        print(date)
    return wrapper
 
@date
def alan():
    print('alan speaking')
@date
def tom():
    print('tom speaking')
 
tom()

如上所示，这样我们就可以减去：tom = date(tom)这一句了，直接调用tom()即可得到想要的结果。
如果我们有其他的类似函数，我们可以继续调用decorator来修饰函数，而不用重复修改函数或者增加新的封装。这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。

装饰器还有更大的灵活性，例如带参数的装饰器：在上面的装饰器调用中，比如@date，该装饰器默认它后面的函数是唯一的参数。
装饰器的语法允许我们调用decorator时，提供其它参数，比如@decorator(a)。
这样，就为装饰器的编写和使用提供了更大的灵活性。
def pre_date(pre):
    def date(func):
        def wrapper():
            func()
            date = datetime.utcnow()
            print(pre  + str(date))
        return wrapper
    return date
 
@pre_date('Today is :')
def alan():
    print ('alan speaking')
 
@pre_date('I am Tom :')
def tom():
    print ('tom speaking')
 
alan()

上面的pre_date是允许参数的装饰器。它实际上是对原有装饰器的一个函数封装，并返回一个装饰器。我们可以将它理解为一个含有环境参量的闭包。
当我们使用@pre_date('Today is :')调用的时候，Python能够发现这一层的封装，并把参数传递到装饰器的环境中。

装饰器的参数除了允许基本类型，还允许 类 作为参数：
from datetime import datetime
# Create your tests here.
class params:
    def __init__(self):
        print("init called")
 
    @staticmethod
    def released():
        print("release this class")
 
 
def pre_date(cls):
    def date(func):
        def wrapper():
            print("before %s ,we called (%s)." % (func.__name__,cls))
            try:
                func()
                date = datetime.utcnow()
                print (date)
            finally:
                cls.released()
        return wrapper
    return date
 
@pre_date(params)
def alan():
    print ('alan speaking')
 
@pre_date(params)
def tom():
    print ('tom speaking')

alan()

这里把类params作为参数传入装饰器中，其中我们用到了@staticmethod这个内置的装饰器，作用是把类中定义的实例方法变成静态方法。
内置的装饰器有三个，分别是staticmethod、classmethod和property，作用分别是把类中定义的实例方法变成静态方法、类方法和类属性.。
再来看看类装饰器，相比函数装饰器，具有灵活度大，高内聚、封装性等优点。

使用类装饰器还可以依靠类内部的 __call__ 方法，当使用 @ 形式将装饰器附加到函数上时，就会调用此方法。
class Foo:
    def __init__(self, func):
        self._func = func
 
    def __call__(self):
        print ('class decorator runing')
        self._func()
        print ('class decorator ending')
 
@Foo
def bar():
    print ('bar')
 
bar()

另一个例子
import time
 
def timeslong(func):
    def call():
        start = time.clock()
        print("It's time starting ! ")
        func()
        print("It's time ending ! ")
        end = time.clock()
        return "It's used : %s ." % (end - start)
    return call

@timeslong
def f():
    y = 0
    for i in range(10):
        y = y + i + 1
        print(y)
    return y

print(f())
