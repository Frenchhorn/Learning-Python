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
