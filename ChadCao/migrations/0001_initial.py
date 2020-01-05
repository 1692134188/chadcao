# Generated by Django 3.0.2 on 2020-01-04 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='学生姓名')),
                ('age', models.IntegerField(default=18, verbose_name='年龄')),
            ],
        ),
    ]