# Generated by Django 3.1.4 on 2024-02-18 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nestquest', '0010_auto_20240218_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housingrequest',
            name='housing_offer',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='nestquest.housingoffer'),
        ),
    ]
