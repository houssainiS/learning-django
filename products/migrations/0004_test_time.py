# Generated by Django 5.1.4 on 2025-01-20 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
