# Generated by Django 2.2.3 on 2019-07-11 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memberships', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membership',
            name='membership',
            field=models.CharField(choices=[('Yearly', 'yrl'), ('Monthly', 'mon'), ('Universe', 'uni')], default='Universe', max_length=30),
        ),
    ]