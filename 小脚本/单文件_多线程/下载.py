import requests
import threading

#单文件，多线程下载
class downloader:
    #构造函数
    def __init__(self):
        #下载的网址
        self.url = 'https://img.acg.moe/common/5/50/Bungo_Stray_Dogs_Main2.jpg'
        #线程数
        self.num = 8
        #文件名
        self.name = self.url.split('/')[-1]
        #仅获取头文件，用于确定文件大小
        r = requests.head(self.url)
        self.total = int(r.headers['Content-Length'])
        print('文件大小为%d字节'%self.total)
    def get_range(self):
    #每个线程的下载内容范围分配
        ranges = []
        #每个线程下载
        offset = (self.total//self.num)
        for i in range(self.num):
            if i == self.num - 1:
                ranges.append((i * offset, self.total))
            else:
                ranges.append((i * offset, (i + 1) * offset))
        return ranges

    def download(self, start, end):
    #下载器
        headers = {'Range':'Bytes=%s-%s'%(start, end), 'Accept-Encoding':'*'}
        #头部信息，指定要下载的部分
        res =requests.get(self.url, headers=headers)
        self.fd.seek(start)
        #移动光标到要开始写入的地方
        self.fd.write(res.content)
        #写入文件
        print('%s:%s 下载成功'%(start, end))
    def run(self):
        self.fd = open(self.name, 'wb')
        #创建文件
        thread_list = []
        #线程池
        n = 0
        for ran in self.get_range():
            start, end = ran
            print('线程%d 下载%s : %s'%(n, start, end))
            n += 1
            thread = threading.Thread(target = self.download, args=(start, end))
            thread.start()
            thread_list.append(thread)
        for i in thread_list:
            i.join()
        print('下载文件%s成功'%self.name)
        self.fd.close()

if __name__ == '__main__':
    down = downloader()
    down.run()
