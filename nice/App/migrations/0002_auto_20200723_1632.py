# Generated by Django 3.0.2 on 2020-07-23 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='china',
            name='sum_cure',
            field=models.IntegerField(default=0, verbose_name='总共治愈人数'),
        ),
        migrations.AddField(
            model_name='china',
            name='sum_die',
            field=models.IntegerField(default=0, verbose_name='总共死亡人数'),
        ),
    ]
