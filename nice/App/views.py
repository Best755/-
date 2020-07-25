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
            data["date"] = date
            data["sum_definite"] = sum_definite
            s.append(data)
        dist["data"]=s
        return JsonResponse(data=dist)


def china_data(request):
    if request.method == "GET":
        sum_data=china.objects.filter(date="2020-07-22")
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