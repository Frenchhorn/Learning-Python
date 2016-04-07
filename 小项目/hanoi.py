#汉诺塔
def hanoi(n,x='A',y='B',z='C'):
    if n == 1:
        print(x + '->' + z)
    else:
        hanoi(n-1,x, z, y)
        print(x + '->' + z)
        hanoi(n-1,y, x, z)
        
hanoi(3)
