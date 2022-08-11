from django.urls import path, re_path

import app1.views
from app1 import views as views

urlpatterns = [
    path('', views.index),  # 根目录
    path('index', views.index),  # 精确匹配
    path('article/<int:id>', views.article),  # 匹配一个参数
    # 匹配两个参数和一个slug
    path('articles/<int:year>/<int:month>/<slug:slug>/', views.article_detail),
    # 正则匹配4个字符的年份
    re_path('articles/(?P<year>[0-9]{4}/)', views.year_archive),
    path('get_name', app1.views.get_name),
    path('get_current_time', views.current_datetime),
    path('person_detail/<str:pk>', views.person_detail)
]
