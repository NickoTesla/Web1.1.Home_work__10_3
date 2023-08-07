from django.urls import path

from .import views 

app_name = "quotes"

urlpatterns = [
    path('', views.main, name="root"),
    path('<int:page>', views.main, name="root_paginate"),
    path('detail/<str:author_fullname>', views.detail, name='detail'),
    path('tag/<str:tag_name>', views.detail_tag, name='detail_tag')
]

