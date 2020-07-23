# Generated by Django 3.0.2 on 2020-07-23 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_anhui_beijin_chongqing_fujian_gansu_guangdong_guangxi_hainan_hebei_heilongjiang_henan_hubei_hunan_ji'),
    ]

    operations = [
        migrations.CreateModel(
            name='sanxi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='时间')),
                ('add_new', models.IntegerField(default=0, verbose_name='新增确诊人数')),
                ('sum_definite', models.IntegerField(default=0, verbose_name='总共确诊人数')),
                ('sum_suspected', models.IntegerField(default=0, verbose_name='现有确诊人数')),
                ('sum_cure', models.IntegerField(default=0, verbose_name='总共治愈人数')),
                ('sum_die', models.IntegerField(default=0, verbose_name='总共死亡人数')),
                ('province_name', models.CharField(max_length=255, verbose_name='地区名称')),
            ],
        ),
    ]