# Generated by Django 3.0.5 on 2020-04-14 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnews', '0003_auto_20200414_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='adv',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
