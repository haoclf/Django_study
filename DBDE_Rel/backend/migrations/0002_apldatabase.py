# Generated by Django 2.0.7 on 2019-02-28 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='aplDatabase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('deleted_at', models.DateTimeField(null=True)),
                ('dbtype', models.CharField(max_length=20, verbose_name='数据库类型')),
                ('dbstructure', models.CharField(max_length=10, verbose_name='数据库架构')),
                ('dbname', models.CharField(max_length=10, verbose_name='数据库名')),
                ('username', models.CharField(max_length=64, verbose_name='用户名')),
                ('shandow', models.CharField(max_length=64, verbose_name='密码')),
                ('cm', models.CharField(max_length=10, verbose_name='CPU/Mem')),
                ('disksize', models.CharField(max_length=10, verbose_name='磁盘容量')),
                ('note', models.CharField(max_length=128, verbose_name='备注')),
            ],
            options={
                'verbose_name_plural': '数据库申请',
                'db_table': 'aplDatabase',
                'verbose_name': '数据库申请',
            },
        ),
    ]
