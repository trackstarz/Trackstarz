# Generated by Django 2.2.3 on 2019-07-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0009_auto_20190729_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='displayname',
            field=models.TextField(blank=True, null=True),
        ),
    ]