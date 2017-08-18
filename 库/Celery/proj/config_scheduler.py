broker_url = 'redis://localhost:6379/3'
result_backend = 'redis://localhost:6379/2'

timezone = 'Asia/Shanghai'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'proj.tasks.add',
        'schedule': timedelta(seconds=30),
        'args': (16, 16)
    },
}