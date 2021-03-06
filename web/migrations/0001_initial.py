# Generated by Django 3.2.5 on 2021-07-13 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='employee_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=5, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('id_card', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('hire_date', models.DateField(blank=True, null=True)),
                ('resign_data', models.DateField(blank=True, null=True)),
                ('imgset_dir', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_photo', models.CharField(blank=True, max_length=200, null=True)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=200, null=True)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10, null=True)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.IntegerField(blank=True, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.IntegerField(blank=True, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='oldperson_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=5, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('id_card', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_data', models.DateField(blank=True, null=True)),
                ('imgset_dir', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_photo', models.CharField(blank=True, max_length=200, null=True)),
                ('room_number', models.CharField(blank=True, max_length=50, null=True)),
                ('firstguardian_name', models.CharField(blank=True, max_length=50, null=True)),
                ('firstguardian_relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('firstguardian_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('firstguardian_wechat', models.CharField(blank=True, max_length=50, null=True)),
                ('sceondguardian_name', models.CharField(blank=True, max_length=50, null=True)),
                ('secondguardian_relationship', models.CharField(blank=True, max_length=50, null=True)),
                ('secondguardian_phone', models.CharField(blank=True, max_length=50, null=True)),
                ('secondguardian_wechat', models.CharField(blank=True, max_length=50, null=True)),
                ('health_state', models.CharField(blank=True, max_length=50, null=True)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=50, null=True)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10, null=True)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.IntegerField(blank=True, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.IntegerField(blank=True, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='sys_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('real_name', models.CharField(blank=True, max_length=50, null=True)),
                ('sex', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('mobile', models.CharField(blank=True, max_length=50, null=True)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=200, null=True)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10, null=True)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.CharField(blank=True, max_length=50, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1, null=True)),
                ('DATAFILTER', models.CharField(blank=True, max_length=200, null=True)),
                ('theme', models.CharField(blank=True, max_length=45, null=True)),
                ('defaultpage', models.CharField(blank=True, max_length=45, null=True)),
                ('logoimage', models.CharField(blank=True, max_length=45, null=True)),
                ('qqopenid', models.CharField(blank=True, max_length=100, null=True)),
                ('appversion', models.CharField(blank=True, max_length=10, null=True)),
                ('jsonauth', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='volunteer_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('ORG_ID', models.IntegerField(blank=True, null=True)),
                ('CLIENT_ID', models.IntegerField(blank=True, null=True)),
                ('username', models.CharField(max_length=50, null=True)),
                ('gender', models.CharField(blank=True, max_length=5, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('id_card', models.CharField(blank=True, max_length=50, null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('checkin_date', models.DateField(blank=True, null=True)),
                ('checkout_data', models.DateField(blank=True, null=True)),
                ('imgset_dir', models.CharField(blank=True, max_length=200, null=True)),
                ('profile_photo', models.CharField(blank=True, max_length=200, null=True)),
                ('DESCRIPTION', models.CharField(blank=True, max_length=200, null=True)),
                ('ISACTIVE', models.CharField(blank=True, max_length=10, null=True)),
                ('CREATED', models.DateTimeField(blank=True, null=True)),
                ('CREATEBY', models.IntegerField(blank=True, null=True)),
                ('UPDATED', models.DateTimeField(blank=True, null=True)),
                ('UPDATEBY', models.IntegerField(blank=True, null=True)),
                ('REMOVE', models.CharField(blank=True, max_length=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='event_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_type', models.IntegerField(blank=True, null=True)),
                ('event_date', models.DateField(auto_now=True, null=True)),
                ('event_location', models.CharField(blank=True, max_length=200, null=True)),
                ('event_desc', models.CharField(max_length=200, null=True)),
                ('oldperson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='web.oldperson_info')),
            ],
        ),
    ]
