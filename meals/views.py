from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from .models import Meals , Category
from blog.models import Post

# Create your views here.


def home(request):

    meal_list = Meals.objects.all()
    category_list = Category.objects.all()
    blog_list = Post.objects.all()
    context = {
        "meal_list" : meal_list,
        "category_list" : category_list,
        "blog_list" : blog_list,
        
        }

    return render(request , 'meals/home.html' , context)    



def meal_list(request):
    meals = Meals.objects.all()
    categories = Category.objects.all()
    context = {
        "meals" : meals,
        "categories" : categories
        }
    return render(request , 'meals/list.html' , context)



def meal_detail(request , slug):
    
    try:
        meal_detail = Meals.objects.get(slug = slug)
    except meal_detail.DoesNotExist:
        meal_detail = None    
    context = {"meal_detail" : meal_detail}
    return render(request , 'meals/detail.html' , context)


def meal_search(request):

    meals = Meals.objects.all()
    allCategories = Category.objects.all()

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            meals = Meals.objects.filter(name__icontains = name)
    if 'categories' in request.GET:
        categories = request.GET['categories']
        if categories:
            meals = Meals.objects.filter(category__name__icontains=categories)

    if 'price-min' in request.GET:
        minPrice = request.GET['price-min']
        maxPrice = request.GET['price-max']
        if minPrice and maxPrice:
            cars = Meals.objects.filter(price__gte = minPrice , price__lte = maxPrice) 
    context = {
        "categories" : allCategories,
        "meals" : meals}

    return render(request , 'meals/search.html' , context)               

            





