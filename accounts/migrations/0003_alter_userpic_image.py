# Generated by Django 5.0.6 on 2024-06-10 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userpic_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpic',
            name='image',
            field=models.ImageField(upload_to='images/%Y/%m/%d/'),
        ),
    ]
