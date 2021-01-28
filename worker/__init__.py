# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Theme   ：
# @Time    : 2021/1/26 22:54
# @Author  :xiaowu
import os
from celery import Celery

from swiper import settings
from worker import config

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

celery_app = Celery('tasks')
celery_app.config_from_object(config)
celery_app.autodiscover_tasks(packages=settings.INSTALLED_APPS)
