from .unjson import unJson
from web.models import *
from rest_framework import viewsets, generics
from web.serializer import *


# 管理员
class EventViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径
    """
    queryset = event_info.objects.all()
    serializer_class = EventSerializer


class EventList(generics.ListCreateAPIView):
    """
        get:
            Return all projects.

        post:
            Create a new project.
    """
    queryset = event_info.objects.all()
    serializer_class = EventSerializer


class EventDetail(generics.RetrieveUpdateAPIView):
    """
        get:
            Return a project instance.

        put:
            Update a project.

        patch:
            Update one or more fields on an existing project.

    """
    queryset = event_info.objects.all()
    serializer_class = EventSerializer



