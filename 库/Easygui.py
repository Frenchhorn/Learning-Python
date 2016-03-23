'''
学习自FishC
'''


# 1. 注意事项
'''
不要在IDLE上运行EasyGui。
因为EasyGui是运行在Tkinter上并拥有自身的事件循环，而IDLE也是Tkinter写的一个应用程序并也拥有自身的事件循环。
因此当两者同时运行时，有可能会发生冲突，且带来不可预测的结果。
因此当你发现你的EasyGui程序有这样的问题时，尝试在IDLE外运行你的程序。
'''

'''
# 2. 一个简单的例子
import easygui as g
import sys
while True:
    g.msgbox('嗨，欢迎进入第一个界面小游戏')  #弹出一个message窗口，只有一个OK选项
    
    msg = '学什么？'
    title = '小游戏互动'
    choices = ['编程', '琴棋书画', '数学']
    
    choice = g.choicebox(msg, title, choices)  #弹出一个Choice窗口，把选择的结果返回给choice，选择Cancel则返回None
    
    g.msgbox('你的选择是：' + str(choice), '结果')  #弹出一个message窗口
    
    msg = '你希望重新开始游戏吗？'
    title = '请选择'
    
    if g.ccbox(msg, title):  #显示一个Continue/Cancel窗口
        pass  #选择Continue
    else:
        sys.exit(0)
'''
'''
# 3. EasyGui的各种功能演示
import easygui as g
g.egdemo()
#可以查看尝试各种功能
'''
'''
# 4. 导入EasyGui
#1
import easygui
#2
from easygui import *
#3
import easygui import g
'''
'''
# 5. 使用EasyGui
#导入完成，GUI操作就是简单的调用EasyGui函数的几个参数的问题了。
#Hello World
import easygui as g
g.msgbox('Hello, world!')
'''

# 6.EasyGui的默认参数
对于所有函数而言，前两个参数是消息和标题，而其它的参数几乎都有简单的默认值。

# 7.使用关键字参数调用EasyGui的函数

# 8.各个按钮组件
## 8.1 msgbox()
msgbox(msg='Your message goes here', title='', ok_button='OK', image=None, root=None)
msgbox显示一个消息和提供一个'OK'按钮，你可以指定任意消息、标题和OK按钮的内容。

## 8.2 ccbox()
ccbox(msg='Shall I continue?', title='', choices=('Continue', 'Cancel'), image=None)
ccbox()提供一个选择：Continue或者Cancel，并相应的返回1(选择Continue)或者0(选择Cancel)
ccbox()返回的是整型的1或0，而不是布尔类型的True或False。但依然可以正常写if ccbox(): ... else:

## 8.3 ynbox()
ynbox(msg='Shall I continue?', title='', choices=('Yes','No'), image=None)
同上

## 8.4 buttonbox()
buttonbox(msg='', title='', choices=('Button1', 'Button2', 'Button3'), image=None, root=None)
可以使用buttonbox()定义自己的一组按钮，buttonbox()会显示一组你定义好的按钮。
当用户点击任意一个按钮时, buttonbox()会返回按钮的文本内容。如果用户按取消或关闭窗口，那会返回第一个选项。

## 8.5 indexbox()
indexbox(msg='Shall I continue?', title='', choices=('Button1', 'Button2', 'Button3'), image=None)
基本跟上面一样，区别在当选择第一份按钮时返回0，第二个返回1，第三个返回2，默认返回0。

## 8.6 boolbox()
boolbox(msg='Shall I continue?', title=' ', choices=('Yes', 'No'), image=None)
选第一个按钮返回1，否则返回0。

# 9.如何在按钮组件里面显示图片
给image参数赋值，仅支持gif文件


# 10为用户提供一系列选项
## 10.1 choicebox()
choicebox(msg='Pick something.', title='', choices=())

## 10.2 multchoicebox()
multchoicebox(msg='Pick as many items as you like.', title='', choices=(), **kwargs)


# 11.让用户输入信息
## 11.1 enterbox()
enterbox(msg='Enter something.',title='', default='', strip='True', image=None, root=None)
提供一个最简单的输入框，返回值为用户输入的字符串。默认返回值会去掉首尾的空格。

## 11.2 integerbox()
intergerbox(msg='', title='', default='', lowerbound=0, upperbound=99, image=None, root=None, **invalidKeywordArguments)
为用户提供一个简单的输入框，只能输入范围内的整数，否则要求用户重新输入。

## 11.3 multenterbox()
multenterbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())

# 12. 输入密码
让用户输入的信息看上去都是******
## 12.1 passwordbox()
passwordbox(msg='Enter your password.', title=' ', default='', image=None, root=None)
跟enerbox()样式一样

## 12.2 multpasswordbox()
multpasswordbox(msg='Fill in values for the fields.', title=' ', fields=(), values=())
跟multenterbox()样式一样，只有最后一个输入框显示为密码形式。


# 13. 显示文本
## 13.1 textbox()
textbox(msg='', title=' ', text='', codebox=0)
text可以是字符串、列表或者元组。

## 13.2 codebox()
codebox(msg='', title=' ', text='')
以等宽字体显示，相当于textbox(codebox=1)


# 14. 目录与文件
## 14.1 diropenbox()
diropenbox(msg=None, title=None, default=None)
提供一个对话框，返回用户选择的目录名(带完整路径)，如果选择Canncel则返回None。
default用于设置默认的打开目录

## 14.2 fileopenbox()
fileopenbox(msg=None, title=None, default='*', filetypes=None)
提供一个对话框，返回用户选择的文件名(带完整路径)，如果选择Canncel则返回None。
关于default参数：
    default='c:/fishc/*.py'即显示C:\fishc文件夹下所有Python文件
    default='c:/fishc/test*.py'即显示C:\fishc文件夹下所有test开头的Python文件
关于filetypes参数：
    可以是字符串列表，如 filetypes = ['*.txt']
    可以在列表中包含列表，列表的最后一项是文件类型的描述，如 filetypes = ['*.css', ['*.htm','html','HTML files']]

## 14.3 filesavebox()
filesavebox(msg=None, title=None, default='', filetypes=None)
提供一个对话框，用于选择文件的保存路径，选择Cancel则返回None。


# 15. 

# 16. 捕获异常
exceptionbox()