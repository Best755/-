# Generated by Django 3.0.2 on 2020-07-23 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_auto_20200723_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='anhui',
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
        migrations.CreateModel(
            name='beijin',
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
        migrations.CreateModel(
            name='chongqing',
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
        migrations.CreateModel(
            name='fujian',
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
        migrations.CreateModel(
            name='gansu',
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
        migrations.CreateModel(
            name='guangdong',
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
        migrations.CreateModel(
            name='guangxi',
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
        migrations.CreateModel(
            name='hainan',
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
        migrations.CreateModel(
            name='hebei',
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
        migrations.CreateModel(
            name='heilongjiang',
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
        migrations.CreateModel(
            name='henan',
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
        migrations.CreateModel(
            name='hubei',
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
        migrations.CreateModel(
            name='hunan',
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
        migrations.CreateModel(
            name='jiangsu',
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
        migrations.CreateModel(
            name='jiangxi',
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
        migrations.CreateModel(
            name='jielin',
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
        migrations.CreateModel(
            name='liaoning',
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
        migrations.CreateModel(
            name='neimenggu',
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
        migrations.CreateModel(
            name='ningxia',
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
        migrations.CreateModel(
            name='qinghai',
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
        migrations.CreateModel(
            name='shandong',
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
        migrations.CreateModel(
            name='shanghai',
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
        migrations.CreateModel(
            name='shanxi',
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
        migrations.CreateModel(
            name='sichuan',
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
        migrations.CreateModel(
            name='tianjing',
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
        migrations.CreateModel(
            name='xinjiang',
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
        migrations.CreateModel(
            name='xizang',
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
        migrations.CreateModel(
            name='yunnan',
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
        migrations.CreateModel(
            name='zejiang',
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