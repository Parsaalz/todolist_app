# Generated by Django 5.0.6 on 2024-06-01 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardpage', '0005_rename_d0_projects_do'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='do',
            field=models.BooleanField(default=True),
        ),
    ]
