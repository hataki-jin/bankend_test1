"""
WSGI config for bankend_test1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bankend_test1.settings')

# 这里要增加这一行代码，类似于环境变量的path
sys.path.append('/var/www/html/safe')

application = get_wsgi_application()
