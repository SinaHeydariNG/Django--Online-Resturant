from pyexpat import model
from django.shortcuts import render
from .models import Reservation
from . import forms
from sitedetails.models import SiteDetails

# Create your views here.


def reserve_table(request):
    reserve_form = forms.ReservationForm()

    if request.method == "POST":
        reserve_form = forms.ReservationForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()

    site_info = SiteDetails.objects.last() 
    context = {
        "site_info" : site_info,
        "form" : reserve_form}        

    return render(request , 'reservation/reserve.html' , context )        


    