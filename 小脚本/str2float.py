# -*- coding: utf-8 -*-

#字符串含小数点转换成浮点数

from functools import reduce

def str2float(s):
    def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,}[s]
        sl=s.split('.')#以小数点分割
        sint = reduce(lambda x,y:10*x+y,map(char2num,sl[0]))#整数部分,10进位
		sfloat = reduce(lambda x,y:10*x+y,map(char2num,sl[1]))*0.1**len(sl[1])#当作整数部分,再整体移到小数位置
		return sint+sfloat
print('str2float(\'123.456\') =', str2float('123.456'))