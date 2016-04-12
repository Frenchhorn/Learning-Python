def a(x):
    if n == 1:
        return 1
    return a(x-1)*x

#改为尾递归后
def a(x):
    return _a(x,1)

def _a(x,y):
    if x == 1:
        return y
    return _a(x-1,x*y)

#Python解释器没有做相关的优化，所以即使把递归改为尾递归也一样会导致栈溢出
