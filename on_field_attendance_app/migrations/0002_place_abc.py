# Generated by Django 2.0.2 on 2018-08-08 09:58

from django.db import migrations
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('on_field_attendance_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='abc',
            field=location_field.models.plain.PlainLocationField(blank=True, max_length=63, null=True),
        ),
    ]