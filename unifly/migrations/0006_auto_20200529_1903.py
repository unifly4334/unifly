# Generated by Django 3.0.6 on 2020-05-29 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webnews', '0005_adv_advside'),
    ]

    operations = [
        migrations.DeleteModel(
            name='tabledata1',
        ),
        migrations.DeleteModel(
            name='tabledata2',
        ),
        migrations.DeleteModel(
            name='tablehead',
        ),
        migrations.RemoveField(
            model_name='newsinfo',
            name='newsid',
        ),
        migrations.AlterField(
            model_name='newsinfo',
            name='newstext1',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='newsinfo',
            name='newstext2',
            field=models.TextField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='newsinfo',
            name='newstext3',
            field=models.TextField(blank=True, max_length=2000, null=True),
        ),
    ]
