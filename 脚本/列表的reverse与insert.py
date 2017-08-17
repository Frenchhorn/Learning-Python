import time

# 先append再reverse的速度比直接insert要快很多倍
# append: O(n)
# insert: O(n^2)
count = 10**5

# 先append,再reverse
# 线性增长
nums = []
a = time.clock()
for i in range(count):
    nums.append(i)
nums.reverse()
print(time.clock() - a)

# 直接用insert插入头部
# 二次方增长
nums = []
a = time.clock()
for i in range(count):
    nums.insert(0, i)
print(time.clock() - a)