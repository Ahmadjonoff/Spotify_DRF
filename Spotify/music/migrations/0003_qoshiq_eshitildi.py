# Generated by Django 4.0.3 on 2022-04-05 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_qoshiq_davomiylik'),
    ]

    operations = [
        migrations.AddField(
            model_name='qoshiq',
            name='eshitildi',
            field=models.PositiveIntegerField(default=0),
        ),
    ]