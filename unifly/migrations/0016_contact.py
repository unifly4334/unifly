# Generated by Django 3.0.6 on 2020-06-22 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnews', '0015_university'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('subject', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=2000)),
            ],
        ),
    ]