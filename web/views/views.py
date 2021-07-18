from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from rest_framework.decorators import api_view
import json

from web import models
from web.models import *
from web.views.cookie import create_token
from web.views.unjson import unJson

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status as st


# Create your views here.

def index(request):
    return render(request, 'web/index.html')


def room(request, client_name):
    return render(request, 'web/room.html', {
        'client_name': client_name
    })


def test(request):
    return HttpResponse("test")


# class Login(APIView):
def login(request):
    # def get(self, request, *args, **kwargs):
    if request.method == "GET":
        return HttpResponse("login test")
    # def post(self, request, *args, **kwargs):
    if request.method == "POST":
        username = request.POST.get('username')
        print(username)
        password = request.POST.get('password')
        print(password)

        try:
            user = Account.objects.filter(username=username,
                                          password=password).first()  # 根据sys_user表的username和password判断是否登录成功
            if user:
                data = {'code': 200, 'token': create_token(username), 'message': 'send succeeded', }
                response = HttpResponse(json.dumps(data))
                # response.set_cookie("token", create_token(data.account), 1800)
                print(response)
                return response
        except IOError:
            print('2333')
        else:
            data = {'code': 403, 'message': '用户名或密码错误'}
            response = HttpResponse(json.dumps(data))
            print('用户名或密码错误')
            return response

# def register(request):
#     if request.method == 'GET':
#         return render(request, 'register.html')
#     if request.method == 'POST':
#         username = request.POST.get('请输入用户名')
#         password = request.POST.get('请输入密码')
#         repeat_password = request.POST.get('请输入确认密码')
#         if not username:
#             return HttpResponse('用户名不能为空')
#         if not password:
#             return HttpResponse('密码不能为空')
#         if not repeat_password:
#             return HttpResponse('确认密码不能为空')
#         if username and password and repeat_password:
#             if password == repeat_password:
#                 # filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表
#                 user_project = models.User.objects.filter(username=username).first()
#                 if user_project:
#                     return HttpResponse('用户名已存在')
#                 else:
#                     models.User.objects.create(username=username, password=password).save()
#                     return redirect(reverse("web:login"))
#             else:
#                 return HttpResponse('两次输入的密码不一致')


# @api_view(['POST'])
# def LoginIn(request):
#     """
#     登录
#     :param request:
#     {username}账户名
#     :return:
#     """
#     data = unJson(request.data)
#     print(data)
#     try:
#         user = sys_user.objects.filter(username=data.username, password=data.password)  # 根据sys_user表的username和password判断是否登录成功
#         if user:
#             data = {'code': 200, 'token': create_token(data.username), 'message': 'send succeeded', }
#             response = HttpResponse(json.dumps(data))
#             # response.set_cookie("token", create_token(data.account), 1800)
#             response.status_code = 200
#             print(response)
#             return response
#     except IOError:
#         print('2333')
#     else:
#         data = {'code': 403, 'message': '用户名或密码错误'}
#         response = HttpResponse(json.dumps(data))
#         print('用户名或密码错误')
#         return response
