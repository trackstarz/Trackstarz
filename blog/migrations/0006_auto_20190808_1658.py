# Generated by Django 2.2.3 on 2019-08-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190808_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burst',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
    ]
