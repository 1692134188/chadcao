# Generated by Django 3.0.2 on 2020-01-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChadCao', '0004_auto_20200110_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
