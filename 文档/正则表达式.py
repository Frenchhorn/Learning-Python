#正则表达式（Regular expressions）

#元字符
元字符，它们并不能匹配自身，它们定义了字符类、子组匹配和模式重复次数等，即特殊功能。
. ^ $ * + ? {} [] \ | ()

#[]
它们指定一个字符类用于存放你需要匹配的字符集合。
可以单独列出，也可以通过两个字符和横杆-
[abc]等价于[a-c]
'在[]内元字符不会触发特殊功能，它们能匹配自身'
'例外^：[^5]会匹配除5以外的任何字符，^称为脱字符合'

#\
反斜杠\的作用跟Python的字符串规则一样，\后加元字符，
那元字符的特殊功能就不会触发。
反斜杠后跟一些字符可以表达特殊的意义：
\d  匹配任何十进制数字；相当于类[0-9]
\D  与\d相反，匹配任何非十进制数字的字符；类[^0-9]
\s  匹配任何空白字符（包括空格、换行符、制表符等）；类[\t\n\r\f\v]
\S  与\s相反，匹配任何非空白字符；类[^\t\n\r\f\v]
\w  匹配任何单词字符；类[a-zA-Z0-9_]
\W  与\w相反
\b  匹配单词的开始或结束，用于确定字符串边界
\B  与\b相反


#*
它用于指定前一个字符匹配0次或多次
例如：ca*t将匹配ct(0个a)，cat（1个a），caaat等


#+
它用于指定前一个字符匹配1次或多次

#?
它用于指定前一个字符匹配0次或1次

#{m,n}  m,n都是十进制整数
它用于指定前一个字符匹配m到n次
{,n}相当于{0,n};{m,}相当于{m,+无穷};{n}则为重复n次
'{}中不要随意加空格'

#.
匹配除换行符以外的所有字符

#|
或操作符，对两个正则表达式进行或操作


#^  \A（MULTILINE不生效的^）
只匹配字符串的起始位置，在MULTILINE中，每遇到换行符则立即进行匹配

#$   \Z
匹配字符串的结束位置


#()
分组

#\1
反向引用，\1表示引用前边成功匹配的序号为1的子组


#使用正则表达式
>>> import re
>>> p = re.compile('ab*')
>>> p  
<_sre.SRE_Pattern object at 0x...>

re.compile也可以接受flags参数，开启特殊功能和语法变化
正则表达式作为一个字符串传入re.compile()
为避免一些不必要的麻烦，所以使用原始字符串来表达正则表达式
即在字符串前加r

#实例匹配
当你将正则表达式编译后，你就得到一个模式对象。
其方法有：
match()   判断一个正则表达式是否从开始处匹配一个字符串
search()  遍历字符串，找到正则表达式匹配的第一个位置
findall() 遍历字符串，找到正则表达式匹配的所有字符，并以列表的形式返回
finditer()遍历字符串，找到正则表达式匹配的所有字符，并以迭代器形式返回
如果没有找到匹配对象，match()和search()会返回None
匹配成功则返回一个匹配对象(match object)包含所有匹配信息
例如从哪开始，到哪结束，匹配的子字符串等

#例子：
>>> import re
>>> p = re.compile('[a-z]+')
>>> p
re.compile('[a-z]+')
>>> p.match("")
>>> print(p.match(""))
None
>>> m = p.match('fishc')
>>> m  
<_sre.SRE_Match object; span=(0, 5), match='fishc'>

现在m是一个匹配对象(match object)，它的信息都存放在m中
#匹配对象的方法和属性
方法    功能
group() 返回匹配的字符串
start() 返回匹配的开始位置
end()   返回匹配的结束位置
span()  返回一个元组表示匹配位置（开始，结束）

>>> m.group()
'fishc'
>>> m.start()
0
>>> m.end()
5
>>> m.span()
(0, 5)

'由于match()只检测字符串的起始位置是否匹配，所以start()总是0

#模块级别的函数
match(),search(),findall(),sub()等同时是全局函数
它们的第一个参数是正则表达式字符串，其它参数则是跟对应的方法采用一样的参数，返回值也一样。
>>> print(re.match(r'From\s+', 'From_FishC.com'))
None
>>> re.match(r'From\s+', 'From FishC.com')
<_sre.SRE_Match object; span=(0, 5), match='From '>


#编译标志
编译标志可以让你改变正则表达式的工作方式。
多个标志可以用|来分割如re.I|re.M

标志            含义
ASCII, A        使转义符号如\w,\b,\s和\d只能匹配ASCII字符
DOTALL,S        使得.匹配任何符号，包括换行符
IGNORECASE, I   匹配的时候不区分大小写
LOCALE, L       支持当前的语言（区域）设置
MULTILINE, M    多行匹配，影响^和$
VERBOSE, X      启用详细的正则表达式

A：使得\w,\W,\b,\B,\s,\S只匹配ASCII字符，而不匹配完整的Unicode字符
S：使得.可以匹配任何字符，包括换行符。如果不使用这个标志，.将匹配除换行符外的所有字符
M：^将匹配每一行的行首；$将匹配每一行的行尾

X：使用后，空格会被忽略，允许使用注释。增加可读性


#拓展语法
前向肯定断言  (?=...)

前向否定断言  (?!...)
例子：
.*[.].*$  用于匹配文件如:ads.exe  fic.txt等

如果要排除某一或多种拓展名时
.*[.](?!bat$).*$   这样可以排除bat文件

.*[.](?!bat$|exe$).*$  同时排除bat和exe文件
当正则表达式bat在当前位置匹配不成功时，会尝试剩下部分的正则表达式，
如果bat匹配成功，则整个正则表达式失败（因为是否定断言）


#修改字符串

方法     用途
split()  在正则表达式匹配的地方进行分割，并返回一个列表
sub()    找到所有匹配的子字符串，并替换为新的内容
subn()   跟sub()一样，但返回新的字符串以及替换的数目

#split()
>>> re.split('[\W]+', 'Words, words, words.')
['Words', 'words', 'words', '']
>>> re.split('([\W]+)', 'Words, words, words.')
['Words', ', ', 'words', ', ', 'words', '.', '']
>>> re.split('[\W]+', 'Words, words, words.', 1)
['Words', 'words, words.']

#sub()
>>> p = re.compile( '(blue|white|red)')
>>> p.sub( 'colour', 'blue socks and red shoes')
'colour socks and colour shoes'
>>> p.sub( 'colour', 'blue socks and red shoes', count=1)
'colour socks and red shoes'

#subn()
>>> p = re.compile( '(blue|white|red)')
>>> p.subn( 'colour', 'blue socks and red shoes')
('colour socks and colour shoes', 2)
>>> p.subn( 'colour', 'no colours at all')
('no colours at all', 0)

空匹配只有在它们没有紧挨着前一个匹配时才会被替换：
>>> p = re.compile('x*')
>>> p.sub('-', 'abxd')
'-a-b-d-'

>>> p = re.compile('section{ ( [^}]* ) }', re.VERBOSE)
>>> p.sub(r'subsection{\1}','section{First} section{second}')
'subsection{First} subsection{second}'

(?P<name>)  指定命名组
\g<name>   引用命名组


替换函数将十进制数替换为十六进制数
>>> def hexrepl(match):
...     "Return the hex string for a decimal number"
...     value = int(match.group())
...     return hex(value)
...
>>> p = re.compile(r'\d+')
>>> p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code.')
'Call 0xffd2 for printing, 0xc000 for user code.'

#非贪婪的限定符
*?  +?  ??  {m,n}?
它们会尽可能地匹配小的文本





