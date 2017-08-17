import time

# 检查两个字符串之间是否存在字符变位(比如"debit card"与"bad credit")
str_a, str_b = 'asdfasdf'*10000, 'aassddff'*10000


# 1.利用字典统计字符出现次数，进行对比
dict_a = {}
dict_b = {}
time_1 = time.clock()
for i in str_a:
    if dict_a.get(i):
        dict_a[i] = dict_a[i] + 1
    else:
        dict_a[i] = 1
for i in str_b:
    if dict_b.get(i):
        dict_b[i] = dict_b[i] + 1
    else:
        dict_b[i] = 1
if dict_a == dict_b:
    print('方法1: 存在字符变位', end=' ')
    print('耗时: ' + str(time.clock()-time_1))


# 2.利用collections.Counter统计字符出现次数，进行对比
from collections import Counter
time_2 = time.clock()
if (Counter(str_a).most_common() == Counter(str_b).most_common()):
    print('方法2: 存在字符变位', end=' ')
    print('耗时: ' + str(time.clock()-time_2))


# 3.按照其中一个字符串的顺序跟另一个字符串进行对比
temp = str_b
same = True
time_3 = time.clock()
for i in str_a:
    if i in temp:
        temp = temp.replace(i, '', 1)
    else:
        same = False
        break
if temp == '' and same:
    print('方法3: 存在字符变位', end=' ')
    print('耗时: ' + str(time.clock()-time_3))
