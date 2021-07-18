# 【channels】（第2步）设置默认路由在项目创建routing.py文件
from django.conf.urls import url
from django.urls import re_path

from . import clients

websocket_urlpatterns = [
    url(r'ws/link/(?P<client_name>\w+)/', clients.ClientConsumer.as_asgi()),
]
