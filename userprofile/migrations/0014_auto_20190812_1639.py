# Generated by Django 2.2.3 on 2019-08-12 16:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0013_auto_20190812_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='displayname',
            field=models.CharField(default=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL), max_length=40),
        ),
    ]