# Generated by Django 3.0.2 on 2020-01-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChadCao', '0003_auto_20200110_2229'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(auto_created=1, blank=True, primary_key=True, serialize=False),
        ),
    ]
