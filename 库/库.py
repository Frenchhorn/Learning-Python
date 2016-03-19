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


#math库       数学库
pi            pi的近似值，15位小数
e             e的近似值，15位小数
log(x)        以e为基的对数
log10(x)      以10为基的对数  #没有log34(x)之类的
log2(x)       以2为基的对数
sqrt(x)       平方根
factorial(x)  阶乘，即x!
degrees(x)    将弧度值转换成角度
radians(x)    将角度值转换成弧度
gcd(x,y)      返回x和y的最大公约数
hypot(x,y)    返回欧几里得距离,即sqrt(x*x, y*y)
isinf(x)      如果是正或负无穷，返回True；其它浮点数则返回False
modf(x)       返回(小数部分,整数部分), 两部分都带与x相同的正负号
sin(x)        正弦函数
cos(x)        余弦函数
tan(x)        正切函数
asin(x)       反正弦函数，x∈[-1.0,1.0]
acos(x)       反余弦函数，x∈[-1.0,1.0]
atan(x)       反正切函数，x∈[-1.0,1.0]
atan2(y,x)    y/x的反正切函数

'''不常用的部分'''
exp(x)        e的x次幂  #相当于e**x
ceil(x)          对浮点数向上取整
floor(x)         对浮点数向下取整
pow(x,y)         计算x的y次方  #本身就有pow()，相当于x**y, pow(x,y,z)相当于x**y%z
copysign(x,y)    返回x值的绝对值与y值的正负号
erf(x)           自变量为x的误差函数
erfc(x)          余补误差函数
expm1(x)         exp(x)-1
fmod(x,y)        浮点数求余，与x%y有可能不同
fabs(x)          返回浮点数的绝对值
trunc(x)         返回与0接近的整数值
frexp(x)         返回(m, e), x = m * 2 ** e, m为浮点数, e为整数
fsum(interable)  返回x阵列值得各项和
gamma(x)         伽马函数（欧拉第二积分）的值
lgamma(x)        伽马函数值的绝对值的自然对数
ldexp(x,i)       返回x * (2**i)
log1p(x)         以e为基(1+x)的对数
sinh(x)          双曲正弦函数
cosh(x)          双曲余弦函数
asinh(x)         反双曲正弦函数
acosh(x)         反双曲余弦函数
atanh(x)         反双曲正切函数

isnan(x)         判断是否为NaN(not a number),返回bool
nan              不明


#os模块
#关于文件/目录常用的函数使用方法
os.getcwd()
返回当前工作目录
	
os.chdir(path)
改变工作目录

os.listdir(path='.')
列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）
mkdir(path)
创建单层目录，如该目录已存在抛出异常

os.makedirs(path)
递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突

os.remove(path)
删除文件

os.rmdir(path)
删除单层目录，如该目录非空则抛出异常

os.removedirs(path)
递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常

os.rename(old, new)
将文件old重命名为new

os.system(command)
运行系统的shell命令

os.walk(top)
遍历top路径以下所有的子目录，返回一个三元组：(路径, [包含目录], [包含文件])

以下是支持路径操作中常用到的一些定义，支持所有平台

os.curdir
指代当前目录（'.'）

os.pardir
指代上一级目录（'..'）

os.sep
输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）

os.linesep
当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）

os.name
指代当前使用的操作系统（包括：'posix',  'nt', 'mac', 'os2', 'ce', 'java'）



#os.path模块
#关于路径常用的函数使用方法
os.path.basename(path)
去掉目录路径，单独返回文件名

os.path.dirname(path)
去掉文件名，单独返回目录路径

os.path.join(path1[, path2[, ...]])
将path1, path2各部分组合成一个路径名

os.path.split(path)
分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在

os.path.splitext(path)
分离文件名与扩展名，返回(f_name, f_extension)元组

os.path.getsize(file)
返回指定文件的尺寸，单位是字节

os.path.getatime(file)
返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

os.path.getctime(file)
返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

os.path.getmtime(file)
返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）


以下为函数返回 True 或 False
os.path.exists(path)
判断指定路径（目录或文件）是否存在

os.path.isabs(path)
判断指定路径是否为绝对路径

os.path.isdir(path)
判断指定路径是否存在且是一个目录

os.path.isfile(path)
判断指定路径是否存在且是一个文件

os.path.islink(path)
判断指定路径是否存在且是一个符号链接

os.path.ismount(path)
判断指定路径是否存在且是一个挂载点

os.path.samefile(path1, paht2)
判断path1和path2两个路径是否指向同一个文件


#pickle模块
#用于把列表，字典，元组打包成一个二进制文件
'''创建文件'''
import pickle

a = [1,2,3,4,5] #需要保存的列表
pickle_file = open(r'C\A\列表.pkl','wb') #创建一个文件，文件后缀任意，建议用pkl

pickle.dump(a, pickle_file)  #把列表a保存到文件中

pickle_file.close()


'''调用文件'''
import pickle

pickle_file = open(r'C\A\列表.pkl','rb')
a = pickle.load(pickle_file)

pickle_file.close()


#time 模块
#时间获取和转换
time 模块提供各种时间相关的功能
在 Python 中，与时间处理有关的模块包括：time，datetime 以及 calendar

时间元祖（time.struct_time）：
gmtime()，localtime() 和 strptime() 以时间元祖（struct_time）的形式返回。

索引值（Index）	属性（Attribute） 	        值（Values）
0	        tm_year（年）			例如：2015
1	        tm_mon（月）			1 ~ 12
2	        tm_mday（日）			1 ~ 31
3	        tm_hour（时）			0 ~ 23
4	        tm_min（分）			0 ~ 59
5	        tm_sec（秒）	                0 ~ 61（见下方注1）
6	        tm_wday（星期几）	        0 ~ 6（0 表示星期一）
7	        tm_yday（一年中的第几天）	1 ~ 366
8	        tm_isdst（是否为夏令时）	0， 1， -1（-1 代表夏令时）

注1：范围真的是 0 ~ 61 ；60 代表闰秒，61 是基于历史原因保留。


time.altzone
返回格林威治西部的夏令时地区的偏移秒数；如果该地区在格林威治东部会返回负值（如西欧，包括英国）；对夏令时启用地区才能使用。

time.asctime([t])
接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2015"（2015年12月11日 周二 18时07分14秒）的 24 个字符的字符串。

time.ctime([secs])
作用相当于 asctime(localtime(secs))，未给参数相当于 asctime()

time.gmtime([secs])
接收时间辍（1970 纪元年后经过的浮点秒数）并返回格林威治天文时间下的时间元组 t（注：t.tm_isdst 始终为 0）

time.daylight
如果夏令时被定义，则该值为非零。

time.localtime([secs])
接收时间辍（1970 纪元年后经过的浮点秒数）并返回当地时间下的时间元组 t（t.tm_isdst 可取 0 或 1，取决于当地当时是不是夏令时）

time.mktime(t)
接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）

time.perf_counter()
返回计时器的精准时间（系统的运行时间），包含整个系统的睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。

time.process_time()
返回当前进程执行 CPU 的时间总和，不包含睡眠时间。由于返回值的基准点是未定义的，所以，只有连续调用的结果之间的差才是有效的。

time.sleep(secs)
推迟调用线程的运行，secs 的单位是秒。

time.strftime(format[, t])
把一个代表时间的元组或者 struct_time（如由 time.localtime() 和 time.gmtime() 返回）转化为格式化的时间字符串。如果 t 未指定，将传入 time.localtime()。如果元组中任何一个元素越界，将会抛出 ValueError 异常。
format 格式如下：
格式	含义	备注
%a	本地（locale）简化星期名称	
%A	本地完整星期名称	
%b	本地简化月份名称	
%B	本地完整月份名称	
%c	本地相应的日期和时间表示	
%d	一个月中的第几天（01 - 31）	
%H	一天中的第几个小时（24 小时制，00 - 23）	
%l	一天中的第几个小时（12 小时制，01 - 12）	
%j	一年中的第几天（001 - 366）	
%m	月份（01 - 12）	
%M	分钟数（00 - 59）	
%p	本地 am 或者 pm 的相应符	注1
%S	秒（01 - 61）	注2
%U	一年中的星期数（00 - 53 星期天是一个星期的开始）第一个星期天之前的所有天数都放在第 0 周	注3
%w	一个星期中的第几天（0 - 6，0 是星期天）	注3
%W	和 %U 基本相同，不同的是 %W 以星期一为一个星期的开始	
%x	本地相应日期	
%X	本地相应时间	
%y	去掉世纪的年份（00 - 99）	
%Y	完整的年份	
%z	用 +HHMM 或 -HHMM 表示距离格林威治的时区偏移（H 代表十进制的小时数，M 代表十进制的分钟数）	
%Z	时区的名字（如果不存在为空字符）	
%%	%号本身	
注1：“%p”只有与“%I”配合使用才有效果。
注2：范围真的是 0 ~ 61（你没有看错哦^_^）；60 代表闰秒，61 是基于历史原因保留。
注3：当使用 strptime() 函数时，只有当在这年中的周数和天数被确定的时候 %U 和 %W 才会被计算。
举个例子：
>>> import time as t
>>> t.strftime("a, %d %b %Y %H:%M:%S +0000", t.gmtime())
'a, 24 Aug 2014 14:15:03 +0000'

time.strptime(string[, format])
把一个格式化时间字符串转化为 struct_time。实际上它和 strftime() 是逆操作。
举个例子：
>>> import time as t
>>> t.strptime("30 Nov 14", "%d %b %y")
time.struct_time(tm_year=2014, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=334, tm_isdst=-1)


time.time()
返回当前时间的时间戳（1970 纪元年后经过的浮点秒数）

time.timezone
time.timezone 属性是当地时区（未启动夏令时）距离格林威治的偏移秒数（美洲 >0；大部分欧洲，亚洲，非洲 <= 0）

time.tzname
time.tzname 属性是包含两个字符串的元组：第一是当地非夏令时区的名称，第二个是当地的 DST 时区的名称。


#grahics库
import grahics

GraphWin类
win = GraphWin()
直接创建一个图形窗口，默认为200*200，
标题为Graphics Window,有最小化和关闭按钮。
点(0,0)表示屏幕左上角
X轴正方向为从左往右
Y轴正方向为从上到下

Ponit类
a = (x, y)
x为横坐标，y为纵坐标
方法：
.getX()       返回点的x轴坐标值
.getY()       返回点的y轴坐标值
a.draw(win)   在win上显示点a
