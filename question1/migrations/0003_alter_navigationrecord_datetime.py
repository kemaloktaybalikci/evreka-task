# Generated by Django 4.0.6 on 2022-07-30 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('question1', '0002_rename_navigationreport_navigationrecord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='navigationrecord',
            name='datetime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
