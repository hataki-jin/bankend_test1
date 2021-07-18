"""
ASGI config for bankend_test1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

import channels
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import web.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankend_test1.settings')


# application = get_asgi_application()
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    # Just HTTP for now. (We can add other protocols later.)
    "websocket": AuthMiddlewareStack(
        URLRouter(
            web.routing.websocket_urlpatterns
        )
    ),
})
