# Generated by Django 5.0.6 on 2024-06-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboardpage', '0006_alter_projects_do'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskusers',
            name='alarm',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
