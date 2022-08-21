from multiprocessing import context
from django.shortcuts import redirect, render
from requests import request
from . import models
from .forms import CommentsForm
from django.core.paginator import Paginator
from sitedetails.models import SiteDetails
from django.contrib.auth.models import User
# Create your views here.


def post_list(request):
    site_info = SiteDetails.objects.last() 
    post_list = models.Post.objects.all()
    paginator = Paginator(post_list , 2)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    context = {
         "site_info" : site_info,     
        "post_list" : post_list}   

    return render(request , 'blog/list.html' , context)



def post_detail(request , id):
    site_info = SiteDetails.objects.last() 
    post = models.Post.objects.get(id=id)
    comments = models.Comments.objects.filter(post_id=id)
    categories = models.Category.objects.all()


    context = {"post" : post , "categories" : categories , "comments" : comments  ,    "site_info" : site_info, }
    return render(request , "blog/detail.html" , context)
        

def add_comment(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        post_id = request.POST['post_id']
        email = request.POST['email']
        phone = request.POST['phone']
        text = request.POST['text']
        created = request.POST['created']
        commnet = models.Comments(user_id = user_id , post_id = post_id , email = email , phone = phone , text = text , created = created)
        commnet.save()

        return redirect("blog:blog_list")


         

def post_by_tag(request , tags):
    site_info = SiteDetails.objects.last()
    post_by_tags = models.Post.objects.filter(tags__name__in = {tags})
    context = {"post_list" : post_by_tags ,    "site_info" : site_info, }
    return render(request , 'blog/list.html' , context)



def post_by_category(request , category):
    site_info = SiteDetails.objects.last()
    post_by_category = models.Post.objects.filter(category__name =category)
    context = {"post_list" : post_by_category ,    "site_info" : site_info, }
    return render(request , 'blog/list.html' , context)




