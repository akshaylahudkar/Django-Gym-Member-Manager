# Generated by Django 3.1.2 on 2021-03-14 05:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0029_auto_20210314_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='amount_pending',
        ),
    ]
