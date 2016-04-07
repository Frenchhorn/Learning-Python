def _odd_iter(): #构造一个从3开始的奇数序列
	n=1
	while True:
		n=n+2
		yield n

def _not_divisible(n): #定义筛选函数
	return lambda x: x%n>0

def primes():
	yield 2			 #输出2
	it = _odd_iter() #初始序列
	while True:
		n = next(it) #返回序列的第一个数
		yield next   #输出序列的第一个数
		it = filter(_not_dicisible(n),it) #构造新序列，把序列的第一个数及其倍数的值全部删去

for n in prines():
	if n<1000:
		print(n)
	else:
		break
#