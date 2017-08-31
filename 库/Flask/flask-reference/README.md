## 安装
### 安装virtualenv
>用于创建独立的环境，也可以不用安装      
`pip install virtualenv`    
创建环境    
`virtualenv venv`   
启用环境    
Windows: `venv/Scripts/activate`    
Linux: `source venv/bin/activate`   
关闭环境
`deactivate`

### 安装Flask
`pip install Flask`

## 运行应用，常用于测试
Linux:    
`export FLASK_APP=hello.py`     
`flask run`     
Window:
`set FlASK_APP=hello.py`    
`flask run`

### 让其它电脑可以访问
`flask run --host=0.0.0.0`      

### 设置为debug模式
Linux: `export FLASK_DEBUG=1`      
Window: `set FLASK_DEBUG=1`     
>debug模式主要有以下几个作用     
* 启用debugger
* 启用自动重载
* 启用应用的debug模式

### 文档
http://dormousehole.readthedocs.io/en/latest/index.html
