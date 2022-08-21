from django.urls import path
from . import views



urlpatterns = [
    path('posts/',views.post_list,name="blog_list"),
    path('<int:id>',views.post_detail,name="blog_detail"),
    path('tags/<slug:tags>',views.post_by_tag,name="post_tags"),
    path('category=<slug:category>',views.post_by_category,name="post_categories"),
    path('add_comment',views.add_comment,name="add_comment"),

]