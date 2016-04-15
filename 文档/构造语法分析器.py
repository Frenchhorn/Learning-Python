#语法分析器

#格式规则
'''
关键字: table、row、cell。 
一、
table 起始一个新的表格。
一个文件可以包含无限数量的表格，并且至少包含一个。

二、
table 后的全部字符构成表格标题。
一个表格并不一定要有标题。

三、
row 起始新的表格行。
表格行不能存在于表格之外。
一个表格可以保护无限行，并且至少有一行。

四、
row 后不能跟字符串。

五、
cell 起始新的单元格。
单元格不能存在于表格行之外。
一行可以包括无限格，而且并非必须包含单元格。
不同行可以有不同数量的单元格。

六、
cell 后的全部字符串构成单元格的内容。
一个单元格可以不包含内容。

七、
字符串是由%包围的零个或更多字符组成的序列。
%%表示空串，字符串中的%%表示一个%。

八、
如果table 或 cell 后跟随2个或更多字符串，表示同一个单元格内的不同行。

九、
关键字不区分大小写。

十、
忽略关键字和字符串间的空格。
相邻关键字，相邻字符串间需要空格分隔。

十一、
文件中的任何文本字符，若不是关键字或字符串的一部分，视为错误。
'''

#实例
'''
table %First table%
    row cell %A1% cell %B1% cell %C1% cell %D1%
    row 
    row cell %The previous row was balnk% cell %B3%
    row cell %A4% %second% cell %B4% %line% cell %C4%
    row cell %%%string%%% cell %% cell %%%% cell %%%%%%
'''

#效果
'''
————————————————
        A1    |    B1     |   C1    |    D1   |
————————————————
                |             |           |           |
————————————————
    The ....   |   B3      |          |           |
————————————————
        A4     |   B4      |    C4  |            |
    second  |  line     |          |             |
————————————————
  %string% |            |     %   |   %%   |
————————————————
'''

#正则匹配依据语法分析器所处的状态处理
'''
————————————————————————————————————————————
    匹配   |                                                          状态                                                                       |
————————————————————————————————————————————
              |    空   |              表格内                |                   行内                   |             单元格内             |
————————————————————————————————————————————
table      |                                                 创建新表格，状态改为表格内                                              |
————————————————————————————————————————————
row        |  错误  |  添加新行，状态改为行内   |                  添加新行              |  添加新行，状态改为行内  |
————————————————————————————————————————————
cell         |                     错误                       |  添加新单元格，状态改为格内  |           添加新单元格         |
————————————————————————————————————————————
字符串     |  错误  |          添加表格标题          |                     错误                  |         添加单元格内容       |
————————————————————————————————————————————
非法文本  |                                                                 错误                                                                |
————————————————————————————————————————————
'''
import re
def importtable(filecontents):
    table = None
    row = None
    cell = None
    for match in re.finditer(
        r"""(?ix)\b(?P<keyword>table|row|cell)\b
                 | %(?P<string>[^%]*(?:%%[^%]*)*)%
                 | (?P<error>\S+)""", filecontents):
        if match.group('keyword') != None:
            keyword = match.group('keyword').lower()
            if keyword == 'table':
                table = RECTable()
                row = None
                cell = None
            elif keyword == 'row':
                if table == None:
                    raise Exception('Invalid data: row without table')
                row = table.addRow()
                cell = None
            elif keyword == 'cell':
                if row == None:
                    raise Exception('Invalid data: cell without row')
                cell = row.addCell()
            else:
                raise Exception('Parser bug: unknown keyword')
        elif match.group('string') != None:
            content = match.group('string').replace('%%', '%')
            if cell != None:
                cell.addContent(content)
            elif row != None:
                raise Exception('Invalid data: string after row keyword')
            elif table != None:
                table.addCaption(content)
            else:
                raise Exception('Invalid data: string before table keyword')
        elif match.group('error') != None:
            raise Exception('Invalid data: ' + match.group('error'))
        else:
            raise Exception('Parser bug: no capturing group matched')
    if table == None:
        raise Exception('Invalid data: table keyword missing')
    return table
