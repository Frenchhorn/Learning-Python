# -*- coding: utf-8 -*-

import math

def quadratic(a, b, c):
    x=2*a
    y=-b
    z=math.sqrt(b**2-4*a*c)
    x1=(y+z)/x
    x2=(y-z)/x
    return x1,x2
# 测试:
print(quadratic(2, 3, 1)) # => (-0.5, -1.0)
print(quadratic(1, 3, -4)) # => (1.0, -4.0）