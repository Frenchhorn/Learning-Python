#移动文件
import os
import shutil
from delSomething import delEmtryDir, delTorrent

#
目标文件夹 = [r'D:\动画\一月番',
              r'D:\动画\十月番',]
movedir = []
for i in 目标文件夹:
    movedir.append(list(os.walk(i)))

#
来源文件夹 = [r'D:\Downloads',]
fromdir = []
for i in 来源文件夹:
    fromdir.append(list(os.walk(i)))

'''
os.walk得到的是(['根目录',['文件夹1','文件夹2'],['文件1','文件2']), ('文件夹1'，['文件夹3'],['文件3'])...的生成器
'''


def move_fun(filename, dirsite, file_site):
    a = os.path.join(dirsite, filename)
    if os.path.exists(a):
        print('文件{}已存在'.format(a))
    else:
        shutil.move(file_site,dirsite)
        print('移动: {} -> {}'.format(filename,dirsite))

def get_file_site():
    #返回需要移动的文件地址列表
    file_site_list = []
    torrent_list = []
    for listwalk in fromdir:
        for i in listwalk:
            for j in i[2]:
                if '.mp4' in j or '.mkv' in j:
                #返回后缀为.mp4和.mkv的文件的地址
                    file_site_list.append(os.path.join(i[0],j))
                elif '.torrent' in j:
                    torrent_list.append(os.path.join(i[0],j))
    return [file_site_list, torrent_list]

class Move_ham:

    def ham(self,h1,h2):
        #汉明距离
        if len(h1) > len(h2) + 5 or len(h1) < len(h2) - 5:
        #两字符串长度如果不在±5以内，则返回100
            return 100
        if len(h1) > len(h2):
        #使两字符串长度一样，以短的为标准
            h1 = h1[:len(h2)]
        else:
            h2 = h2[:len(h1)]
        h = 0  
        #计算汉明距离
        for i, j in zip(h1,h2):
            if i != j:
                h += 1
        return h

    def movedir(self, file_name):
        #输入文件名，寻找目标文件夹
        for i in movedir:
            for j in i[1:]:
            #排除根目录，从第一个文件夹开始搜索
                if j[2] != []:
                #如果不为空文件夹，求第一个文件和输入的文件名的汉明距离
                    b = self.ham(j[2][0],file_name)
                    if b < 10:  
                    #汉明距离小于10，返回这个文件夹地址
                        return j[0]

    def start(self):
        a = get_file_site()
        #获得需要移动的文件地址列表
        for i in a[0]:
            b = os.path.basename(i) 
            c = self.movedir(b)  #利用文件名进行目标文件夹的搜索
            if c:
                move_fun(b, c, i)
        delTorrent(a[1])

class Move_nm:
    def __init__(self, n=5):
        self.n = n

    def get_file_sign(self, file_name):
        #得到文件名第一个[]及n-1位
        a = file_name[:file_name.find(']') + self.n]  #第一个[]部分加n-1个字符
        '''
        b = file_name[file_name.find(']')+1:]  #除去第一个[]后剩下的部分
        c = b[:b.find(']')+1]  #第二个[]部分
        '''
        return a

    def movedir(self, file_name):
        #寻找文件的目标文件夹
        a = self.get_file_sign(file_name)  #文件名特征
        for i in movedir:
            for j in i[1:]:
            #排除根目录，从第一个文件夹开始搜索
                if j[2]:
                #如果不为空文件夹，判断两者的文件名特征是否一致，一致则返回文件夹地址
                    b = self.get_file_sign(j[2][0])
                    if a == b:
                        return j[0]

    def start(self):
        a = get_file_site()
        #获得需要移动的文件地址列表
        for i in a[0]:
            b = os.path.basename(i)
            c = self.movedir(b)  #利用文件名进行目标文件夹的搜索
            if c:
                move_fun(b, c, i)
        delTorrent(a[1])

if __name__ == '__main__':
    s = input('输入1为用汉明距离判断，直接回车为[]+4，其它数字为[]+n：')
    if s == '1':
        a = Move_ham()
        a.start()
    elif s == '':
        a = Move_nm()
        a.start()
    else:
        a = Move_nm(int(s))
        a.start()
    delEmtryDir(来源文件夹)
    a = input('按任意按钮退出')