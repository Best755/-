from django.db import models


# Create your models here.
class china(models.Model):
    date = models.DateField(u'时间')
    province_name = models.CharField(u'省份名称', max_length=255, default="")
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)


class word(models.Model):
    date = models.DateField(u'时间')
    word_name = models.CharField(u'国家名称', max_length=255, default="")
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)


class guizhou(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class xinjiang(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class beijin(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class shanghai(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class guangdong(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class neimenggu(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class liaoning(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class shandong(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class sichuan(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class tianjing(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class sanxi(models.Model):
    # 陕西
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class zejiang(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class fujian(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class yunnan(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class jiangsu(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class chongqing(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class hebei(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class shanxi(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class hubei(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class henan(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class hunan(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class anhui(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class heilongjiang(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class jiangxi(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class guangxi(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class hainan(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class gansu(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class jielin(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class ningxia(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class qinghai(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)

class xizang(models.Model):
    date = models.DateField(u'时间')
    add_new = models.IntegerField(u'新增确诊人数', default=0)
    sum_definite = models.IntegerField(u'总共确诊人数', default=0)
    sum_suspected = models.IntegerField(u'现有确诊人数', default=0)
    sum_cure = models.IntegerField(u'总共治愈人数', default=0)
    sum_die = models.IntegerField(u'总共死亡人数', default=0)
    province_name = models.CharField(u'地区名称', max_length=255)