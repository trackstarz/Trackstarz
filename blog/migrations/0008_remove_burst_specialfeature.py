# Generated by Django 2.2.3 on 2019-08-08 17:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_burst_specialfeature'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='burst',
            name='specialfeature',
        ),
    ]