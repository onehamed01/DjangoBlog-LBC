from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>/', views.postdetail, name='postdetail'),
    path('post/form', views.postform, name='postform'),
]