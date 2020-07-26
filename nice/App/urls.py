from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

from App import views

app_name = "User"
urlpatterns = {
    path('index/', views.index, name="index"),
    path('china_data/', views.china_data, name="china_data"),
    path('word_data/', views.word_data, name="word_data"),
    path('word_data_5/', views.word_data_5, name="word_data_5"),
    path('index_ze/', views.index_ze, name="index_ze"),
    path('sum_china_data/', views.sum_china_data, name="sum_china_data"),
    path('china_data_5/', views.china_data_5, name="china_data_5"),
    # path('es/', views.es, name="es"),
    path('es_s/', views.es_s, name="es_s"),
}
