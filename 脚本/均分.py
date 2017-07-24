#把一个序列按每N个元素组成一组，N=3时
a = range(1,9)
list(zip(*[iter(a)]*3))
