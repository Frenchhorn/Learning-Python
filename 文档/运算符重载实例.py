#运算符重载实例

__getitem__(self, key)
#定义获取容器中指定元素的行为，相当于 self[key]
class Indexer:
    def __getitem__(self, index):
        return index**2
X = Indexer()
X[2]  -> 4
for i in range(5):
    print(X[i], end=' ')
0 1 4 9 16
class stepper:
    def __getitem__(self, i):
        return self.data[i]
X = stepper()
X.data = 'Spam"
X[1] -> 'p'
for item in X:
    print(item, end=' ')
S p a m
#在成员关系测试in、列表解析、内置函数map、列表和元组赋值运算
#以及类型构造方法也会自动调用__getitem__

__iter__(self)
#定义当迭代容器中的元素的行为
__next__(self)
#定义next()函数
class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2
for i in Squares(1, 5):
    print(i, end=' ')
1 4 9 16 25

__getattr__(self, attrname):
#拦截属性点号运算
class empty:
    def __getattr__(self, attrname):
        if attrname == 'age':
            return 40
        else:
            raise AttributeError, attrname
X = empty()
X.age -> 40
X.name
...error text omitted...
AttributeError: name

__setattr__(self, attr, value)
#拦截所有属性的赋值
#要用self.__dict__['name'] = x ,而不是self.name = x，不然会引发递归循环
class accesscontrol:
    def __setattr__(self, attr, value):
        if attr == 'age':
            self.__dict__[attr] = value
        else:
            raise AttributeError
X = accesscontrol()
X.age = 40
X.age -> 40
X.name = 'mel'
...text omitted...
AttributeError

__call__
#调用实例时，使用__call__方法
class Callee:
    def __call__(self, *pargs, **kargs):
        print('Called:' , pargs, kargs)
C = Callee()
C(1,2,3)
-> Called: (1, 2, 3) {}
C(1, 2, 3, x=4, y=5)
-> Called: (1, 2, 3) {'y':5, 'x':4}
class Prod:
    def __init_(self, value):
        self.value = value
    delf __call__(self, other):
        return self.value * other
x = Prod(2)
x(3) -> 6
x(4) -> 8

__lt__ 和 __gt__
#定义比较，> 和 <
class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other
X = C()
print(X > 'ham')   #True (run __gt__)
print(X < 'ham')   #False (run __lt__)

__bool__ 和 __len__
#在布尔环境，首先调用__bool__
class Truth:
    def __bool__(self):
        return True
x = Truth()
if x: print('yes')
->yes
#如果没有__bool__，就会调用__len__，非空为真

__del__
#对象析构函数，当实例空间被回收是，会调用__del__
class Life:
    def __init__(self, name='unkown'):
        print('Hello', name)
        self.name = name
    def __del__(self):
        print('Goodbye', name)
a = Life('B')
-> Hello B
a = 'abc'
-> Goodbye B

class T
