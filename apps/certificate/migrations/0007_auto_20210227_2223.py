# Generated by Django 2.2 on 2021-02-27 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0006_auto_20210227_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='email_sent',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='image_created',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
