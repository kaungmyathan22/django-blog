# Generated by Django 2.2 on 2019-05-03 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_auto_20190503_1253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='show_in_footer',
        ),
    ]