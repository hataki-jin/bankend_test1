from django.contrib import admin
from web.models import *

# Register your models here.
admin.site.register(Account)
admin.site.register([oldperson_info, event_info])
admin.site.register(employee_info)
admin.site.register(volunteer_info)
admin.site.register(sys_user)
