from unicodedata import name
from django.urls import path
from . import views



urlpatterns = [
    path('',views.home,name="home"),
    path('meal_list/',views.meal_list,name="meal_list"),
    path('<slug:slug>',views.meal_detail,name="meal_detail"),
    path('search/' , views.meal_search , name='meal_search'),

]