# Generated by Django 5.0.6 on 2024-06-01 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardpage', '0002_projects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='tasks',
            field=models.ManyToManyField(to='dashboardpage.taskusers'),
        ),
    ]