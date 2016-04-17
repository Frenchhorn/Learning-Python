import re

'''
用于匹配下列字符中的任意一个：美元符号$，双引号"，单引号'，换行符，
0-9之间任意数字，正斜杠或者反斜杠。
'''
a = re.compile(r'''[$"'\n\d/\\]''')

'''
把一个字符串中的所有数字替换为该数字的2倍
'''
subject = '123 z 2'
def cal(matchobj):
    return str(int(matchobj.group()) * 2)
reobj = re.compile(r'\d+')
result1 = reobj.sub(cal, subject)
#'246 z 4'

'''
把标签<b></b>内的before替换为after
'''
subject = 'before <b> first before </b>before <b> before </b>'
innerre = re.compile('before')
def replacewithin(matchobj):
    return innerre.sub('after', matchobj.group())
result = re.sub(r'<b>.+?</b>', replacewithin, subject)
#'before <b> first after </b>before <b> after </b>'

'''
拆分字符串，把<b></b>之类的标签去掉，得到拆分后的字符串列表
顺便去掉首尾的空格
'''
subject = 'I like <b>bold</> and <i>italic</i> fonts'
reobj = re.compile(' ?<[^<>]*> ?')
result = reobj.split(subject)
#['I like', 'bold', 'and', 'italic', 'fonts']

'''
同上的情况，但保留<b>这些标签
'''
subject = 'I like <b>bold</> and <i>italic</i> fonts'
reobj = re.compile('(<[^<>]*>)')
result = reobj.split(subject)
#['I like ', '<b>', 'bold', '</>', ' and ', '<i>', 'italic', '</i>', ' fonts']

'''
'''
