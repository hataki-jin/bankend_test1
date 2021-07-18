from django.http import HttpResponse
from rest_framework.decorators import api_view

from .unjson import unJson
from web.models import *
from rest_framework import viewsets, generics
from web.serializer import *


# 用户
class AccountViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountList(generics.ListCreateAPIView):
    """
        get:
            Return all projects.

        post:
            Create a new project.
    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountDetail(generics.RetrieveUpdateAPIView):
    """
        get:
            Return a project instance.

        put:
            Update a project.

        patch:
            Update one or more fields on an existing project.

    """
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# 老人
class OldPersonViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径
    """
    queryset = oldperson_info.objects.all()
    serializer_class = OldPersonSerializer


class OldPersonList(generics.ListCreateAPIView):
    """
        get:
            Return all projects.

        post:
            Create a new project.
    """
    queryset = oldperson_info.objects.all()
    serializer_class = OldPersonSerializer


class OldPersonDetail(generics.RetrieveUpdateAPIView):
    """
        get:
            Return a project instance.

        put:
            Update a project.

        patch:
            Update one or more fields on an existing project.

    """
    queryset = oldperson_info.objects.all()
    serializer_class = OldPersonSerializer


# 员工
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径
    """
    queryset = employee_info.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeList(generics.ListCreateAPIView):
    """
        get:
            Return all projects.

        post:
            Create a new project.
    """
    queryset = employee_info.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDetail(generics.RetrieveUpdateAPIView):
    """
        get:
            Return a project instance.

        put:
            Update a project.

        patch:
            Update one or more fields on an existing project.

    """
    queryset = employee_info.objects.all()
    serializer_class = EmployeeSerializer


# 义工
class VolunteerViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径
    """
    queryset = volunteer_info.objects.all()
    serializer_class = VolunteerSerializer


class VolunteerList(generics.ListCreateAPIView):
    """
        get:
            Return all projects.

        post:
            Create a new project.
    """
    queryset = volunteer_info.objects.all()
    serializer_class = VolunteerSerializer


class VolunteerDetail(generics.RetrieveUpdateAPIView):
    """
        get:
            Return a project instance.

        put:
            Update a project.

        patch:
            Update one or more fields on an existing project.

    """
    queryset = volunteer_info.objects.all()
    serializer_class = VolunteerSerializer


# 管理员
class SysUserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径
    """
    queryset = sys_user.objects.all()
    serializer_class = SysUserSerializer


class SysUserList(generics.ListCreateAPIView):
    """
        get:
            Return all projects.

        post:
            Create a new project.
    """
    queryset = sys_user.objects.all()
    serializer_class = SysUserSerializer


class SysUserDetail(generics.RetrieveUpdateAPIView):
    """
        get:
            Return a project instance.

        put:
            Update a project.

        patch:
            Update one or more fields on an existing project.

    """
    queryset = sys_user.objects.all()
    serializer_class = SysUserSerializer


# @api_view(['GET'])
# def oldIDtoName(request, pk):
#     """老人id换名字"""
#     try:
#         old = oldperson_info.objects.get(pk=pk)
#     except oldperson_info.DoesNotExist:
#         return HttpResponse(status=404)
#     name = old.username
#     return HttpResponse(name)
#
#
# @api_view(['GET'])
# def volunteerIDtoName(request, pk):
#     """义工id换名字"""
#     try:
#         volunteer = volunteer_info.objects.get(pk=pk)
#     except volunteer_info.DoesNotExist:
#         return HttpResponse(status=404)
#     name = volunteer.username
#     return HttpResponse(name)
