# Generated by Django 3.1.3 on 2020-11-28 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='surname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
