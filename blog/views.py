from multiprocessing import context
from django.shortcuts import render
from requests import request
from . import models
from .forms import CommentsForm
from django.core.paginator import Paginator

# Create your views here.


def post_list(request):
    post_list = models.Post.objects.all()
    paginator = Paginator(post_list , 2)
    page = request.GET.get('page')
    post_list = paginator.get_page(page)

    context = {"post_list" : post_list}   

    return render(request , 'blog/list.html' , context)



def post_detail(request , id):
    post = models.Post.objects.get(id=id)
    comments = models.Comments.objects.filter(post=post)
    categories = models.Category.objects.all()

    
    if request.method == "POST":
     
        comment_form = CommentsForm(request.POST)
        if comment_form.is_valid():
            
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.post = post
            new_comment.save()
        else:
            print("Invalid")
    else :
         comment_form = CommentsForm()


    context = {"post" : post , "categories" : categories , "comments" : comments , "comment_form" : comment_form}
    return render(request , "blog/detail.html" , context)
        



         

def post_by_tag(request , tags):
    post_by_tags = models.Post.objects.filter(tags__name__in = {tags})
    context = {"post_list" : post_by_tags}
    return render(request , 'blog/list.html' , context)



def post_by_category(request , category):
    post_by_category = models.Post.objects.filter(category__name =category)
    context = {"post_list" : post_by_category}
    return render(request , 'blog/list.html' , context)




