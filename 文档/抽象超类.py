from abc import ABCMeta, abstractmethod

class Super(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass

class Sub(Super): pass

class Bus(Super):
    def action(self):
        print('创建带action()方法的Super的子类的实例 => 成功')
        
if __name__ == '__main__':
    try:
        X = Super()
    except:
        print('直接创建Super类的实例 => 失败')
    try:
        Y = Sub()
    except:
        print('创建没有带action()方法的Super的子类的实例 => 失败')
    try:
        Z = Bus()
        Z.delegate()
    except:
        print('会失败吗？')
    
