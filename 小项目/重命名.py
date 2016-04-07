#批量改文件名
import os

index = ['01','02','03','04','05','06','07','08','09']  #不能直接01，要加''因为直接01是整型，而在整型中只有1没有01
howmany = 50    #文件数
for i in range(10,101):
    index.append(i)

for a in range(howmany):
    i = r"D:\BaiduYunDownload\{0}.jpg".format(index[a])
    j = r"D:\BaiduYunDownload\{0}.jpg".format(index[a+50])
    os.rename(i,j)
