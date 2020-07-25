import datetime

from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from App.models import word,china


def index(request):
    if request.method == "GET":
        sum_data = word.objects.filter(word_name="美国")
        dist={}
        s=[]
        for item in  sum_data:
            data={}
            date = item.date
            sum_definite = item.sum_definite
            sum_die = item.sum_die
            sum_cure = item.sum_cure
            data["date"] = date
            data["sum_definite"] = sum_definite
            data["sum_cure"] = sum_cure
            data["sum_die"] = sum_die
            s.append(data)
        dist["data"]=s
        return JsonResponse(data=dist)


def china_data(request):
    if request.method == "GET":
        tody = datetime.date.today()
        sum_data=china.objects.filter(date=tody)
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
        # tody = datetime.date.today()
        sum_data=word.objects.filter(date="2020-07-22")
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