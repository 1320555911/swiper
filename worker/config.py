# -*- coding: utf-8 -*-
# @File    : config.py
# @Theme   ：celery配置
# @Time    : 2021/1/26 22:54
# @Author  :xiaowu
broker_url = 'redis://localhost:6379/3'
broker_pool_limit = 10  # Borker 连接池, 默认是10

timezone = 'Asia/Shanghai'
accept_content = ['pickle', 'json']
task_serializer = 'pickle'

result_backend = 'redis://localhost:6379/3'
result_serializer = 'pickle'
result_cache_max = 1000  # 任务结果最大缓存数量
result_expires = 3600  # 任务结果过期时间
worker_redirect_stdouts_level = 'INFO'