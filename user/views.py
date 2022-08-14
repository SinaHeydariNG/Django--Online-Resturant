from django.shortcuts import render , redirect
from . import forms
from . import models
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse , HttpResponseRedirect
# Create your views here.


def send_email(request):
    if request.method == "POST":
        form = forms.UserMessage(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(name,message,email,['testing@gmail.com'])

            except BadHeaderError:
                return HttpResponse('invalid header')   

            return redirect('../email_success/')        


    else:
        form = forms.UserMessage()   

    context = {"form" : form}   

    return render(request , 'usermessage/message.html' , context)  


def email_success_sent(request):
    
    return HttpResponse("Your email has been sent successfully !")



def about(request):

    about_site = models.About.objects.get()
    print(about_site.title)
    context = {"about_site" : about_site}
    return render(request , 'about/about.html' , context)
    



