# -*- coding: utf-8 -*-
#请编写一个prod()函数，可以接受一个list并利用reduce()求积：
from functools import reduce

def prod(L):
    def multiply(x,y):
        return x*y
    return reduce(multiply,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))