def move(n, a, b, c):
    if n ==1: 
        print("%s----->%s" % (a,c)) 
    else: 
        move(n-1,a,c,b) #需要上一个函数把n-1个盘子从a柱移到b柱上 
        print("%s----->%s" % (a,c)) #把第n个盘子从a柱移到c柱上 
        move(n-1,b,a,c) #把n-1个盘子从b柱移到c柱上