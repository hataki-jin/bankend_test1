"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import path, re_path
from rest_framework.documentation import include_docs_urls
from rest_framework import routers
from .views import base, person, avatar, views
from . import clients
# from .views import base, person, statistics, views, websocket
from rest_framework import routers

urlpatterns = [
    # base
    url(r'^base/login/', base.login),

    # avatar
    url('^avatar/upload/', avatar.uploadAvatar),
    url('^avatar/getimg/(?P<id>.+)/$', avatar.getImg),  # 图片

    # test
    url('^test/', views.test),

    # websocket:channels
    # path('', views.index, name='index'),
    # path('<str:room_name>/', views.room, name='room'),

    # 下面这个用网页测试websocket，可用
    # path('link/<str:client_name>/', views.room, name='room'),

    # test
    path('link/<str:client_name>/', clients.ClientConsumer),

    # websocket deprecated
    # path('refresh', websocket.refresh),
    # path('reboot', websocket.reboot),
]
