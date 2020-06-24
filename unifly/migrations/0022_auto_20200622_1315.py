# Generated by Django 3.0.6 on 2020-06-22 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnews', '0021_auto_20200622_1201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='cname',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
