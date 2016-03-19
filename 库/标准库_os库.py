#os模块中关于文件/目录常用的函数使用方法
os.getcwd()
返回当前工作目录
	
os.chdir(path)
改变工作目录

os.listdir(path='.')
列举指定目录中的文件名（'.'表示当前目录，'..'表示上一级目录）

os.mkdir(path)
创建单层目录，如该目录已存在抛出异常

os.makedirs(path)
递归创建多层目录，如该目录已存在抛出异常，注意：'E:\\a\\b'和'E:\\a\\c'并不会冲突

os.remove(path)
删除文件

os.rmdir(path)
删除单层目录，如该目录非空则抛出异常

os.removedirs(path)
递归删除目录，从子目录到父目录逐层尝试删除，遇到目录非空则抛出异常

os.rename(old, new)
将文件old重命名为new

os.system(command)
运行系统的shell命令，命令行

os.walk(top)
遍历top路径以下所有的子目录，返回一个三元组：[(路径, [包含目录], [包含文件]), (路径, [包含目录], [包含文件])...]

以下是支持路径操作中常用到的一些定义，支持所有平台

os.curdir
指代当前目录（'.'）

os.pardir
指代上一级目录（'..'）

os.sep
输出操作系统特定的路径分隔符（Win下为'\\'，Linux下为'/'）

os.linesep
当前平台使用的行终止符（Win下为'\r\n'，Linux下为'\n'）

os.name
指代当前使用的操作系统（包括：'posix',  'nt', 'mac', 'os2', 'ce', 'java'）


#os.path模块中关于路径常用的函数使用方法
os.path.basename(path)
去掉目录路径，单独返回文件名

os.path.dirname(path)
去掉文件名，单独返回目录路径

os.path.join(path1[, path2[, ...]])
将path1, path2各部分组合成一个路径名

os.path.split(path)
分割文件名与路径，返回(f_path, f_name)元组。如果完全使用目录，它也会将最后一个目录作为文件名分离，且不会判断文件或者目录是否存在

os.path.splitext(path)
分离文件名与扩展名，返回(f_name, f_extension)元组

os.path.getsize(file)
返回指定文件的尺寸，单位是字节

os.path.getatime(file)
返回指定文件最近的访问时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

os.path.getctime(file)
返回指定文件的创建时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）

os.path.getmtime(file)
返回指定文件最新的修改时间（浮点型秒数，可用time模块的gmtime()或localtime()函数换算）


以下为函数返回 True 或 False
os.path.exists(path)
判断指定路径（目录或文件）是否存在

os.path.isabs(path)
判断指定路径是否为绝对路径

os.path.isdir(path)
判断指定路径是否存在且是一个目录

os.path.isfile(path)
判断指定路径是否存在且是一个文件

os.path.islink(path)
判断指定路径是否存在且是一个符号链接

os.path.ismount(path)
判断指定路径是否存在且是一个挂载点

os.path.samefile(path1, paht2)
判断path1和path2两个路径是否指向同一个文件
