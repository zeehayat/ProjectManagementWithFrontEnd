# Generated by Django 5.1.4 on 2025-01-14 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_management', '0003_alter_usernotificationpreference_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usernotificationpreference',
            name='config',
            field=models.JSONField(blank=True, default=dict),
        ),
    ]
