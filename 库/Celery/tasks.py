from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/5', backend='redis://localhost:6379/6') # backend为可选

@app.task
def add(x, y):
    return x + y

# 文档
# http://docs.celeryproject.org/en/latest/getting-started/first-steps-with-celery.html

# 启动
# celery -A tasks worker -l info
