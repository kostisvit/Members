# Generated by Django 4.2 on 2024-06-13 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='First Name', max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='Last Name', max_length=30),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(default='123456789', max_length=15, unique=True),
        ),
    ]