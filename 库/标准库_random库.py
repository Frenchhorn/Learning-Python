#random库         随机数库
seed(x)           给随机数一个种子值，默认随机种子是系统时钟
#设定相同的随机种子后，得到随机数是相同的
random()          生成一个[0,1.0]之间的随机小数
uniform(a,b)      生成一个a到b之间的随机小数
randint(a,b)      生成一个a到b之间的随机整数
randrange(a,b,c)  随机生成一个从a开始到b以c递增的数,c默认为1
choice(<list>)    从列表中随机返回一个元素
shuffle(<list>)   将列表中的元素随机打乱
sample(<list>),k) 从指定列表随机获取k个元素
