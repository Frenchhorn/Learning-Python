#backup.py
import time
import shutil
import os

source = r'C:\Users\lenovo\Desktop\p'
target_dir = r'B:\BACKUP'

try:
    zipFile = shutil.make_archive('Python-'+ time.strftime('%Y%m%d%H%M%S'), 'zip', source)
    shutil.move(zipFile, target_dir)
    print(os.path.join(target_dir, os.path.basename(zipFile)),'备份成功')
except:
    print('备份失败')
a = input()
