# Generated by Django 2.2.3 on 2019-07-30 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0010_userprofile_displayname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='displayname',
            field=models.CharField(default='sean', max_length=40),
        ),
    ]
