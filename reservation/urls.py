from django.urls import path
from . import views

urlpatterns = [
    path('',views.reserve_table,name="add_reserve"),

]