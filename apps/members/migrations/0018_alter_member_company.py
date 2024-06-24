# Generated by Django 4.2 on 2024-06-22 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
        ('members', '0017_alter_member_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='company',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]
