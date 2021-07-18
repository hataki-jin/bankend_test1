from django.db import models


# Create your models here.

class oldperson_info(models.Model):
    id = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(blank=True, null=True)
    CLIENT_ID = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, default='oldperson', unique=True)
    gender = models.CharField(max_length=5, blank=True, null=True)  # f/m
    age = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    id_card = models.CharField(max_length=50, blank=True, null=True)  # 身份证
    birthday = models.DateField(blank=True, null=True)
    checkin_date = models.DateField(blank=True, null=True)
    checkout_data = models.DateField(blank=True, null=True)
    imgset_dir = models.CharField(max_length=200, blank=True, null=True)
    profile_photo = models.CharField(max_length=200, blank=True, null=True)
    room_number = models.CharField(max_length=50, blank=True, null=True)
    firstguardian_name = models.CharField(max_length=50, blank=True, null=True)
    firstguardian_relationship = models.CharField(max_length=50, blank=True, null=True)
    firstguardian_phone = models.CharField(max_length=50, blank=True, null=True)
    firstguardian_wechat = models.CharField(max_length=50, blank=True, null=True)
    sceondguardian_name = models.CharField(max_length=50, blank=True, null=True)
    secondguardian_relationship = models.CharField(max_length=50, blank=True, null=True)
    secondguardian_phone = models.CharField(max_length=50, blank=True, null=True)
    secondguardian_wechat = models.CharField(max_length=50, blank=True, null=True)
    health_state = models.CharField(max_length=50, blank=True, null=True)
    DESCRIPTION = models.CharField(max_length=50, blank=True, null=True)
    ISACTIVE = models.CharField(max_length=10, blank=True, null=True)
    CREATED = models.DateTimeField(blank=True, null=True)
    CREATEBY = models.IntegerField(blank=True, null=True)
    UPDATED = models.DateTimeField(blank=True, null=True)
    UPDATEBY = models.IntegerField(blank=True, null=True)
    REMOVE = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.username


class employee_info(models.Model):
    id = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(blank=True, null=True)
    CLIENT_ID = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, default='employee')
    gender = models.CharField(max_length=5, blank=True, null=True)  # f/m
    phone = models.CharField(max_length=50, blank=True, null=True)
    id_card = models.CharField(max_length=50, blank=True, null=True)  # 身份证
    birthday = models.DateField(blank=True, null=True)
    hire_date = models.DateField(blank=True, null=True)
    resign_data = models.DateField(blank=True, null=True)
    imgset_dir = models.CharField(max_length=200, blank=True, null=True)
    profile_photo = models.CharField(max_length=200, blank=True, null=True)
    DESCRIPTION = models.CharField(max_length=200, blank=True, null=True)
    ISACTIVE = models.CharField(max_length=10, blank=True, null=True)
    CREATED = models.DateTimeField(blank=True, null=True)
    CREATEBY = models.IntegerField(blank=True, null=True)
    UPDATED = models.DateTimeField(blank=True, null=True)
    UPDATEBY = models.IntegerField(blank=True, null=True)
    REMOVE = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.username


class volunteer_info(models.Model):
    id = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(blank=True, null=True)
    CLIENT_ID = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=50, default='volunteer')
    gender = models.CharField(max_length=5, blank=True, null=True)  # f/m
    phone = models.CharField(max_length=50, blank=True, null=True)
    id_card = models.CharField(max_length=50, blank=True, null=True)  # 身份证
    birthday = models.DateField(blank=True, null=True)
    checkin_date = models.DateField(blank=True, null=True)
    checkout_data = models.DateField(blank=True, null=True)
    imgset_dir = models.CharField(max_length=200, blank=True, null=True)
    profile_photo = models.CharField(max_length=200, blank=True, null=True)
    DESCRIPTION = models.CharField(max_length=200, blank=True, null=True)
    ISACTIVE = models.CharField(max_length=10, blank=True, null=True)
    CREATED = models.DateTimeField(blank=True, null=True)
    CREATEBY = models.IntegerField(blank=True, null=True)
    UPDATED = models.DateTimeField(blank=True, null=True)
    UPDATEBY = models.IntegerField(blank=True, null=True)
    REMOVE = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return self.username


class event_info(models.Model):
    id = models.AutoField(primary_key=True)
    event_type = models.IntegerField(blank=True, null=True)
    event_date = models.DateField(auto_now=True, null=True)
    event_location = models.CharField(max_length=200, blank=True, null=True)
    event_desc = models.CharField(max_length=200, null=True)
    oldperson = models.ForeignKey(oldperson_info, on_delete=models.CASCADE,
                                  related_name='person',
                                  blank=True, null=True)

    def __str__(self):
        return self.event_type


class sys_user(models.Model):
    id = models.AutoField(primary_key=True)
    ORG_ID = models.IntegerField(null=True, blank=True)
    CLIENT_ID = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=50, default='sysuser')
    password = models.CharField(max_length=50, default='123456')
    real_name = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=50, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True)
    DESCRIPTION = models.CharField(max_length=200, blank=True, null=True)
    ISACTIVE = models.CharField(max_length=10, blank=True, null=True)
    CREATED = models.DateTimeField(blank=True, null=True)
    CREATEBY = models.CharField(max_length=50, blank=True, null=True)
    UPDATED = models.DateTimeField(blank=True, null=True)
    UPDATEBY = models.CharField(max_length=50, blank=True, null=True)
    REMOVE = models.CharField(max_length=1, blank=True, null=True)
    DATAFILTER = models.CharField(max_length=200, blank=True, null=True)
    theme = models.CharField(max_length=45, blank=True, null=True)
    defaultpage = models.CharField(max_length=45, blank=True, null=True)
    logoimage = models.CharField(max_length=45, blank=True, null=True)
    qqopenid = models.CharField(max_length=100, blank=True, null=True)
    appversion = models.CharField(max_length=10, blank=True, null=True)
    jsonauth = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
