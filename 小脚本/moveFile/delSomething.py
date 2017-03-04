import os

#删除空文件夹
def delEmtryDir(文件夹列表):
    dirList = []
    for theDir in 文件夹列表:    
        for item in os.listdir(theDir):
            if '.' not in item:
                dirList.append(os.path.join(theDir, item))
    for i in dirList:
        try:
            os.rmdir(i)
            print('删除空文件夹{}'.format(i))
        except:
            print('错误：删除文件夹{}时出错,可能是因为里面还有东西...'.format(i))


#删除种子文件
def delTorrent(torrent_list):
    for i in torrent_list:
        os.remove(i)
        print('删除种子文件{}'.format(i))

#test