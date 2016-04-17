class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname]  = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Tom'

if __name__ == '__main__':
    x = Test1()
    y = Test2()
    x.name = 'Bob'
    try:
        y.name = 'Sue'
    except:
        print('x.name无法赋值')
    try:
        x.age = 12
    except:
        print('x.age无法赋值')    
    y.age = 40
