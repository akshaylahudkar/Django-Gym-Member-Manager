# Generated by Django 2.0.3 on 2018-03-16 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_auto_20180315_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='mobile_number',
            field=models.IntegerField(blank=True, unique=True),
        ),
    ]