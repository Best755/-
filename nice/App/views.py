import datetime

from django.db.models import Q
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from elasticsearch import Elasticsearch

from App.models import word, china, china_if


def index(request):
    """美国数据接口"""
    if request.method == "GET":
        sum_data = word.objects.filter(word_name="美国").order_by('-date')
        dist = {}
        s = []
        for item in sum_data:
            data = {}
            date = item.date
            sum_definite = item.sum_definite
            sum_die = item.sum_die
            sum_cure = item.sum_cure
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["sum_cure"] = sum_cure
            data["sum_die"] = sum_die
            s.append(data)
        dist["data"] = s
        return JsonResponse(data=dist)


def china_data(request):
    if request.method == "GET":
        """中国个地区数据接口"""
        tody = datetime.date.today()
        sum_data = china.objects.filter(date=tody)
        dist = {}
        s = []
        for item in sum_data:
            data = {}
            date = item.date
            sum_definite = item.sum_definite
            province_name = item.province_name
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["province_name"] = province_name
            s.append(data)
        dist["data"] = s
        return JsonResponse(data=dist)


def word_data(request):
    if request.method == "GET":
        """世界数据接口"""
        tody = datetime.date.today()
        sum_data = word.objects.filter(date="2020-07-24")
        dist = {}
        s = []
        for item in sum_data:
            data = {}
            date = item.date
            word_name = item.word_name
            sum_definite = item.sum_definite
            sum_die = item.sum_die
            sum_cure = item.sum_cure
            # province_name = item.province_name
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["word_name"] = word_name
            data["sum_die"] = sum_die
            data["sum_cure"] = sum_cure
            # data["province_name"] = province_name
            s.append(data)
        dist["data"] = s
        return JsonResponse(data=dist)


def word_data_5(request):
    if request.method == "GET":
        """世界排名前五"""
        tody = datetime.date.today()
        sum_data = word.objects.filter(date="2020-07-24").order_by('-sum_definite')
        dist = {}
        s = []
        for item in sum_data[0:5]:
            data = {}
            date = item.date
            word_name = item.word_name
            sum_definite = item.sum_definite
            sum_die = item.sum_die
            sum_cure = item.sum_cure
            # province_name = item.province_name
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["word_name"] = word_name
            data["sum_die"] = sum_die
            data["sum_cure"] = sum_cure
            # data["province_name"] = province_name
            s.append(data)
        dist["data"] = s
        return JsonResponse(data=dist)


def index_ze(request):
    if request.method == "GET":
        sum_data = word.objects.filter(word_name="美国")
        dist = {}
        s = []
        for item in sum_data:
            data = {}
            date = item.date
            sum_definite = item.sum_definite
            sum_die = item.sum_die
            sum_cure = item.sum_cure
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["sum_cure"] = sum_cure
            data["sum_die"] = sum_die
            s.append(data)
        dist["data"] = s
        return JsonResponse(data=dist)


def sum_china_data(request):
    if request.method == "GET":
        """数据对比接口"""
        sum_data_china = china_if.objects.filter(date="2020-07-25")
        sum_data_english = word.objects.filter(Q(date="2020-07-25") & Q(word_name="英国"))
        sum_data_german = word.objects.filter(Q(date="2020-07-25") & Q(word_name="德国"))
        dist = {}
        s = []
        for item in sum_data_china:
            data = {}
            date = item.date
            add_new = item.add_new
            sum_definite = item.sum_definite
            sum_die = item.sum_die
            sum_cure = item.sum_cure
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["sum_cure"] = sum_cure
            data["sum_die"] = sum_die
            data["add_new"] = add_new
            data["name"] = "中国"
            s.append(data)
        for items in sum_data_english:
            data = {}
            date = items.date
            add_new = items.add_new
            sum_definite = items.sum_definite
            sum_die = items.sum_die
            sum_cure = items.sum_cure
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["sum_cure"] = sum_cure
            data["sum_die"] = sum_die
            data["add_new"] = add_new
            data["name"] = "英国"
            s.append(data)
        for items in sum_data_german:
            data = {}
            date = items.date
            add_new = items.add_new
            sum_definite = items.sum_definite
            sum_die = items.sum_die
            sum_cure = items.sum_cure
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["sum_cure"] = sum_cure
            data["sum_die"] = sum_die
            data["add_new"] = add_new
            data["name"] = "德国"
            s.append(data)
        dist["data"] = s
        return JsonResponse(data=dist)


def china_data_5(request):
    if request.method == "GET":
        """中国排名前五接口"""
        tody = datetime.date.today()
        sum_data = china.objects.filter(date=tody).order_by('-sum_definite')
        dist = {}
        s = []
        for item in sum_data[0:5]:
            data = {}
            date = item.date
            province_name = item.province_name
            sum_definite = item.sum_definite
            sum_die = item.sum_die
            sum_cure = item.sum_cure
            # province_name = item.province_name
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["province_name"] = province_name
            data["sum_die"] = sum_die
            data["sum_cure"] = sum_cure
            # data["province_name"] = province_name
            s.append(data)
        dist["data"] = s
        return JsonResponse(data=dist)


def es(request):
    if request.method == "GET":
        """es导入数据"""
        tody = datetime.date.today()
        es = Elasticsearch(hosts="47.96.129.100", port=9200)
        # es.indices.create(index="nice", ignore=400)
        word_data = china_if.objects.filter(date="2020-07-28")
        for item in word_data:
            data = {}
            data["name"] = "中国"
            data["add_new"] = item.add_new
            data["sum_definite"] = item.sum_definite
            data["sum_suspected"] = item.sum_suspected
            data["sum_cure"] = item.sum_cure
            data["sum_die"] = item.sum_die
            data["date"] = item.date
            res = es.index(index="nice", doc_type="word", body=data)
        return JsonResponse({"errmsg": "ok"})


def es_s(request):
    if request.method == "GET":
        """es搜索接口"""
        es = Elasticsearch(hosts="47.96.129.100", port=9200)
        name = request.GET.get("name", "中国")
        query = {
            "query": {
                "match": {
                    "name": name
                },
            },
            "sort": [
                {
                    "date": {
                        "order": "desc"
                    }
                }
            ]
        }
        ret = es.search(index='nice', doc_type='word', body=query, size=300)
        s = ret["hits"]["hits"]
        l = []
        a = []
        data = {}
        for i in s:
            data_list = i["_source"]
            if data_list["date"] == "2020-07-23" and data_list["name"] == "中国":
                data_list = {}
                data_list["add_new"] = 0
                data_list["sum_die"] = 4644
                data_list["sum_cure"] = 79112
                data_list["sum_suspected"] = 1521
                data_list["sum_definite"] = 84332
                data_list["name"] = "中国"
                data_list["date"] = "2020-07-23"
            if data_list["name"] == name:
                l.append(data_list)
        if name == "中国":
            data["data"] = l[0:5]
        else:
            data["data"] = l[1:6]
        return JsonResponse(data=data, json_dumps_params={'ensure_ascii': False})
