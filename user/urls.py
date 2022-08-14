from django.urls import path 
from . import views



urlpatterns = [
    path('about/',views.about,name='about'),
    path("send_email/",views.send_email,name='send_email'),
    path("email_success/",views.email_success_sent,name='email_success')

]