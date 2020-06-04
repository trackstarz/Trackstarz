# Generated by Django 2.2.3 on 2019-08-29 14:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20190828_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentlike',
            name='comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentlikes', to='blog.Comment'),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentlikers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='replylike',
            name='reply',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replylikes', to='blog.Reply'),
        ),
        migrations.AlterField(
            model_name='replylike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replylikers', to=settings.AUTH_USER_MODEL),
        ),
    ]