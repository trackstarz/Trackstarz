# Generated by Django 2.2.3 on 2019-08-13 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofile', '0020_auto_20190813_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(),
        ),
    ]
