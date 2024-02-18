# Generated by Django 3.1.4 on 2024-02-18 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nestquest', '0006_auto_20240218_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to=settings.AUTH_USER_MODEL),
        ),
    ]
