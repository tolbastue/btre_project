from django.urls import path

from . import views

urlpatterns = [
    # 1st param: path
    # 2nd param: function (method)
    # 3rd param: name for accessing this path
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
]