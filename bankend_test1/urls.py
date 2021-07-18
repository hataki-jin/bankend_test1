"""bankend_test1 URL Configuration

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
from django.contrib import admin
from django.urls import path, include

from web.views import avatar
from web.views.views import *
from web.views.person import *
from web.views.event import *

from rest_framework import routers
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = routers.DefaultRouter()
router.register(r'accounts', AccountViewSet)
router.register(r'oldpersons', OldPersonViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'volunteers', VolunteerViewSet)
router.register(r'sysusers', SysUserViewSet)
router.register(r'events', EventViewSet)
# router.register(r'web/login', view.Login)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [

    # swagger/
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # admin/
    path('admin/', admin.site.urls),

    # api/
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # api/web/
    path('api/web/', include('web.urls')),

    # WEBSOCKET
    # url('websocket/link', websocket.link),
    # url('websocket/send', websocket.send),
    # url('websocket/refresh', websocket.refresh),
    # url('websocket/cameraLink', websocket.cameraLink),
    # url('websocket/reboot', websocket.reboot),
    # url('websocket/entering', websocket.entering),
    # url('websocket/changeFuc', websocket.changeFuc),
    # url('websocket/takePhoto', websocket.takePhoto),
    # url('websocket/standard', websocket.standard),
    # url('websocket/total', websocket.totalNum),
]
