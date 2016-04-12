#TempConvert_loop.py
#实例一
'''
for i in range(3):
    val = input("请输入带温度表示符号的温度值（例如：32C，45F）：")
    if val[-1] in ['c','C']:
        f = 1.8*float(val[0:-1])+32
        print("转换后的温度为：%.2fF" %f)
    elif val[-1] in ['f','F']:
        c = (float(val[0:-1])-32)/1.8
        print("转换后的温度为：%.2fC" %c)
    else:
        print("输入有误")
'''
#实例二
class Celsius:
    def __init__(self, value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        self.value = float(value)


class Fahrenheit:
    def __get__(self, instance, owner):
        return instance.cel *1.8 +32
        #instance.cel是指TempConvert的实例化对象的cel属性

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8

class TempConvert:
    cel = Celsius()
    fah = Fahrenheit()
