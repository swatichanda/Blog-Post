from django.contrib import admin
from django.urls import path
from blog_api.views import BlogPostList, BlogPostDetail

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('create/', BlogPostList.as_view(), name='blogpost_list'),
    path('create/<int:pk>/', BlogPostDetail.as_view(), name='blogpost_detail'),
]
