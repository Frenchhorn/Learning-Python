> [文档](http://python.jobbole.com/84041/)

### 启动(与proj文件夹同一级下执行)
`celery -A proj worker -l info`

### 定时任务
配置文件为`config_scheduler.py`

启动 celery需要加上-B 参数`celery -A proj worker -B -l info`

-B 不能在Windows下使用
