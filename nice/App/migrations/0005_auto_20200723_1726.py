# Generated by Django 3.0.2 on 2020-07-23 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_province'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='word_name',
            field=models.CharField(default='', max_length=255, verbose_name='国家名称'),
        ),
        migrations.AlterField(
            model_name='province',
            name='sum_suspected',
            field=models.IntegerField(default=0, verbose_name='总共疑是人数'),
        ),
    ]