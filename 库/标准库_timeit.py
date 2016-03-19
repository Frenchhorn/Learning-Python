#timeit模块
timeit模块--准确测量小段代码的执行时间

timeit模块提供了测量Python小段代码执行时间的方法，它既可以在命令行界面直接使用，
也可以通过导入模块进行调用。该模块灵活地避开了测量执行时间所容易出现的错误。

以下是命令行界面的使用方法：
$ python -m timeit '"-".join(str(n) for n in range(100))'
10000 loops, best of 3: 40.3 usec per loop
$ python -m timeit '"-".join([str(n) for n in range(100)])'
10000 loops, best of 3: 33.4 usec per loop
$ python -m timeit '"-".join(map(str, range(100)))'
10000 loops, best of 3: 25.2 usec per loop

以下是IDLE下调用的方法：
>>> import timeit
>>> timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
0.8187260627746582
>>> timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
0.7288308143615723
>>> timeit.timeit('"-".join(map(str, range(100)))', number=10000)
0.5858950614929199

需要注意的是，只有当使用命令行界面时，timeit才会自动确定重复的次数。

#timeit模块的3个实用函数和1个公共类

#timeit.timeit(stmt='pass',setup='pass',timer=<deault timer>,number=1000000)
创建一个Timer实例，参数分别为stmt(需要测量的语句或函数)
,setup(初始化代码或构建环境的导入语句)，
timer(计时函数),number(每一次测量中语句被执行的次数)
#例子
>>> import timeit
>>> timeit.timeit('char in text', setup='text = "I love FishC.com!"; char = "o"')
0.41440500499993504
>>> timeit.timeit('text.find(char)', setup='text = "I love FishC.com!"; char = "o"')
1.7246671520006203

#timeit.repeat(stmt='pass',setup='pass',timer=<deault timer>,repeat=3,number=1000000)
重复测试，返回一个包含每次时间的列表

#timeit.print_exc(file=None)
输出计时代码的回溯


#class timeit.Timer(stmt='pass',setup='pass',timer=<timer function>)
计算小段代码执行速度的类，构造函数需要的参数有stmt(需要测量的语句或函数)，
setup(初始化代码或构建环境的导入语句)，timer(计时函数)。
前两参数默认为'pass'，timer参数是平台相关的；前两个参数可以包含多个语句，
多个语句间使用分号(;)或新行隔开。
例子
>>> import timeit
>>> t = timeit.Timer('char in text', setup='text = "I love FishC.com!"; char = "o"')
>>> t.timeit()
0.3955516149999312
>>> t.repeat()
[0.40193588800002544, 0.3960157959998014, 0.39594301399984033]


#如何进行多行语句的测量
def test():
    """Stupid test function"""
    L = [i for i in range(100)]

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))
