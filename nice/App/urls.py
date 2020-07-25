from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from App import views

app_name = "User"
urlpatterns = [
    path('index/', views.index, name="index"),
    path('china_data/', views.china_data, name="china_data"),
    path('word_data/', views.word_data, name="word_data"),
]
