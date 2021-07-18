from django.shortcuts import render
from .cookie import *
import datetime
from .unjson import unJson
from rest_framework.views import APIView
from rest_framework import status, generics
from django.http import Http404

import json

from ..models import *
from ..serializer import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import HttpResponse


@api_view(['POST'])
def uploadAvatar(request):
    """
    上传接口 type：0 代表老人 1 代表工作人员 2 代表义工
    :param request:
    :return:
    """
    upload_file = request.FILES['file']
    request.data.pop('file')
    try:
        person_type = request.POST.get('type')  # type = 0:老人 1:员工 2:义工
        img_id = request.POST.get('id')
    except BaseException:
        return HttpResponse('type 和 id 为必填字段, type 0:老人 1:员工 2:义工')

    try:
        print(img_id)
        if person_type == '0':
            person_type = "oldperson"
            obj = oldperson_info.objects.get(pk=img_id)
            serializer = OldPersonSerializer(obj)
        elif person_type == '1':
            person_type = "employee"
            obj = employee_info.objects.get(pk=img_id)
            serializer = EmployeeSerializer(obj)
        elif person_type == '2':
            person_type = "volunteer"
            obj = volunteer_info.objects.get(pk=img_id)
            serializer = VolunteerSerializer(obj)
        else:
            return HttpResponse('type 和 id 为必填字段, type 0:老人 1:员工 2:义工')
    except employee_info.DoesNotExist or oldperson_info.DoesNotExist or volunteer_info.DoesNotExist:
        return HttpResponse('找不到该' + person_type)

    print(upload_file)
    url = './img/avatar/' + person_type + img_id + '-' + upload_file.name
    file = open(url, 'wb+')
    for chunk in upload_file.chunks():
        file.write(chunk)

    obj.profile_photo = url
    obj.save()
    # if serializer.is_valid():
    #     serializer.validated_data['profile_photo'] = url
    #     serializer.save()

    return Response(serializer.data)


# 获取照片，id为imgid
@api_view(['GET'])
def getImg(request, img_id):
    result = img_id
    print(result)
    path = './' + result
    image_data = open(path, "rb").read()
    return HttpResponse(image_data, content_type="image/jpg")
