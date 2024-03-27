from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('articles', views.articles, name="articles"),
    path('tamarix', views.tamarix, name="tamarix"),
    path('tamarix/records', views.tamarix_preview, name="tamarix_records"),
    path('process_client/', views.process_client, name="process_client"),

]