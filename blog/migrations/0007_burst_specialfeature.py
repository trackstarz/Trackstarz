# Generated by Django 2.2.3 on 2019-08-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20190808_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='burst',
            name='specialfeature',
            field=models.BooleanField(default=False),
        ),
    ]
