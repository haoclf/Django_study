#  -*- coding:utf-8 -*-

import os
from celery.task import task
from celery import shared_task

@task
def logCeleryOper():
    with open('/tmp/celeryOper.log','a+') as fa:
        fa.write('Task success!')


@task()
def run_test(tk):
    print('hello %s' % tk)
    result = True
    return result

@shared_task()
def celeryTouch(mes):
    with open('/tmp/celryTouch.txt','a+') as fa:
        fa.write(mes)
