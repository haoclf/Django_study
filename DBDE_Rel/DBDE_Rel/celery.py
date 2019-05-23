from __future__ import absolute_import
from celery import Celery
from django.conf import settings

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','DBDE_Rel.settings')

#app = Celery('backend',
app = Celery('DBDE_Rel',
             broker=settings.CELERY_BROKER_URL,
             backend='redis://127.0.0.1:6379/0'
             #backend='redis'
)

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


#BROKER_URL = 'redis://127.0.0.1:6379/0'  #Broker配置，使用redis作为消息中间件
#CELERY_RESULT_SERIALIZER = 'json'  #结果序列化方案
#CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24  #任务过期时间
#CELERY_TIMEZONE = 'Asia/Shanghai'  #时区设置
#CELERY_IMPORTS = (   #指定导入的任务模块，可以指定多个
#    'project.tasks',
#)
