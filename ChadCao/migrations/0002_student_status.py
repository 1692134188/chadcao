# Generated by Django 3.0.2 on 2020-01-10 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChadCao', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.IntegerField(default=1, verbose_name='状态'),
        ),
    ]
