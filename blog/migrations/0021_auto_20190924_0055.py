# Generated by Django 2.2.3 on 2019-09-24 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0020_auto_20190829_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burst',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile'),
        ),
    ]