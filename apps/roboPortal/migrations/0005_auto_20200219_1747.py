# Generated by Django 2.1.7 on 2020-02-19 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roboPortal', '0004_auto_20200219_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem_statement',
            name='description',
            field=models.TextField(default='', max_length=10000),
        ),
        migrations.AlterField(
            model_name='problem_statement',
            name='requirements',
            field=models.TextField(max_length=10000),
        ),
    ]
