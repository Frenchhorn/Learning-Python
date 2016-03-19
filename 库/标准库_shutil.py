#shutil库
用于处理文件

abspath(path)
返回绝对路径
shutil.abspath('.')
->'C:\\Users\\lenovo\\Desktop\\p\\一些实例'

chown(path, user=None, group=None)
改变文件的所有者的用户和组

copy(src, dst, *, foollow_symlinks=True)
src是source,即文件文件；dst是destination,即目录地址
复制文件scr到目录dst,返回dst\文件名
copy data and mode bits

    copy2(src, dst, *, foollow_symlinks=True)
    同copy
    copy data and all stat info

    copyfile(src, dst, *, follow_symlinks=True)
    同copy
    复制文件内容
    shutil.copyfile(r'D:\1.txt',r'D:\2.txt')
    把1的内容复制到2中，会覆盖2中的内容

    copyfileobj(fsrc, fdst, length=16384)
    copy data from file-like object fsrc to file-like object fdst
    分块复制，以免占用太多内存

    copymode(src, dst, *, follow_symlinks=True)
    同copy
    copy mode bits
    
    copystat(src, dst, *, follow_symlinks=True)
    同copy
    copy all stat info(mode bits, atime, mtime, flags)
    拷贝文件(包括时间戳)

    copytree

        ignore_patterns(*patterns)
        Function that can be used as copytree() ignore parameter

disk_usage(path)
返回磁盘的空间使用情况
shutil.disk_usage(r'D:')
->usage(total=431624286208, used=402654621696, free=28969664512)
单位为bytes,除以1024^3即为GB

errno
标准errno系统符号

fnmatch
Filename matching with shell patterns

get_archive_formats()
->[('bztar', "bzip2'ed tar-file"), ('gztar', "gzip'ed tar-file"), ('tar', 'uncompressed tar file'), ('zip', 'ZIP file')]
可压缩或解压的格式列表

    get_unpack_formats()
    ->[('bztar', ['.bz2'], "bzip2'ed tar-file"), ('gztar', ['.tar.gz', '.tgz'], "gzip'ed tar-file"), ('tar', ['.tar'], 'uncompressed tar file'), ('zip', ['.zip'], 'ZIP file')]
    可解压的格式列表

get_terminal_size(fallback=(80, 24))
Get the size of the terminal window

make_archive(base_name, format, root_dir=None, base_dir=None, verbose=0, dry_run=0, owner=None, group=None, logger=None)
压缩文件
base_name为压缩后的名字(不含后缀名),format为压缩格式(zip等),root_dir为压缩的目录地址

move(src, dst)
移动文件或文件夹到另一个文件夹中

rmtree(path, ignore_errors=False, onerror=None)
递归删除目录树 #文件夹中即使有文件也一样会删除

unpact_archive(filename, extract_dir=None, format=None)
解压文件
filename为文件地址，extract_dir为解压的目标目录，format为解压格式，不填默认为文件名后缀

register_archive_format(name)
unregister_archive_format(name)
register_unpack_format(name)
unregister_unpack_format(name)
