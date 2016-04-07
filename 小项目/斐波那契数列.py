def fibo(number):
    a=[1,1]
    for i in range(number):
        if i>1:
            a.append(a[i-1]+a[i-2])
    return a

def fibo_2(number):
    a = []
    def fibo_inner(number):
        if number == 0:
            return 1
        elif number == 1:
            return 1
        else:
            return fibo_inner(number-1)+fibo_inner(number-2)
    for i in range(number):
        a.append(fibo_inner(i))
    return a

	
