# Generated by Django 2.0.2 on 2018-08-08 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('on_field_attendance_app', '0003_auto_20180808_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='comment',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]