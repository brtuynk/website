# Generated by Django 3.1.3 on 2020-11-28 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_project_surname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='name',
        ),
    ]