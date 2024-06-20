# Generated by Django 4.2 on 2024-06-20 10:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0007_subscription_active_subscription_subscription_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='company',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='member',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscription',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
    ]
