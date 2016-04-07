#插入排序
#从小到大
number = input('输入多少个数字？')
a = []
for i in range(int(number)):
    a.append(float(input()))
b = len(a)
for i in range(1,b):
    while i > 0:
        if a[i] < a[i-1]:
            a[i],a[i-1] = a[i-1],a[i]
        i -= 1
print(a)
