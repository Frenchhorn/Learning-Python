
# coding: utf-8

# # you-get使用

# 下载视频（合集/单集）、音乐（单曲/专辑）、图片，主要用cmd来下载，但也可以用于制作脚本批量下载时使用。下面主要介绍一些主要的命令行操作。

# In[1]:

import os


# 1.直接下载，会在命令行的当前目录下创建文件，如果是下载合集，还会创建文件夹。

# In[2]:

#下载
os.system('you-get http://music.163.com/#/album?id=2943405')


# 2.查看详细信息，一般包含文件名、格式、大小，可能会有分辨率选择，可以按相关提示选择分辨率

# In[ ]:

#查看信息
os.system('you-get -i http://music.163.com/#/album?id=2943405')
os.system('you-get --info http://music.163.com/#/album?id=2943405')


# In[ ]:

#选择分辨率，如果显示的信息里面有的话,一般是没有的
os.system('you-get --itag=18 https://www.youtube.com/watch?v=jNQXAC9IVRw')


# 3.暂停和重新开始下载
# 
# 下载到一半，如果突然暂停或按Ctrl + C停止，可以重新输入再下载，程序会自动检测已下载的部分。如果要用强制重新下载，可以加上`--force`/`-f` 。

# 4.设置下载目录和下载的文件名，方便用于写脚本

# In[ ]:

#设置下载目录和下载的文件名称
os.system('you-get -O 1.mp4 https://www.youtube.com/watch?v=jNQXAC9IVRw')
os.system('you-get -o C:\\Users\lenovo\Desktop\music http://music.163.com/#/album?id=2943405')
#--output-dir/-o option to set the path, and --output-filename/-O to set the name of the downloaded file


# 5.设置代理,默认为系统的环境变量http_proxy

# In[ ]:

os.system('you-get -x 127.0.0.1:8087 https://www.youtube.com/watch?v=jNQXAC9IVRw')


# 6.不下载，直接用播放器或浏览器看，vlc为播放器名，chromium为浏览器

# In[ ]:

os.system('you-get -p vlc https://www.youtube.com/watch?v=jNQXAC9IVRw')
os.system('you-get -p chromium https://www.youtube.com/watch?v=jNQXAC9IVRw')


# 7.载入cookie，现仅支持Mozilla和 Netscape

# In[ ]:

os.system('you-get -c https://www.youtube.com/watch?v=jNQXAC9IVRw')


# 可以输入关键词，会直接google搜索相关的第一个视频下载。
