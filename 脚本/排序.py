def my_sort(a):
	b=len(a)
	for i in range(b):
		for j in a[range(i,b)]:
			if a[i]>a[j]:
				c=a[i]
				a[i]=a[j]
				a[j]=c

	
def insertion_sort(list):
	for index in range(1,len(list)):
		value = list[index]
		i = index - 1
		while i>=0: and (value < list[i]):
			list[i+1] = list[i]
			list[i] = value
			i = i - 1

