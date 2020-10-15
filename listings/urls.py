from django.urls import path

from . import views

urlpatterns = [
    # 1st param: path
    # 2nd param: function (method)
    # 3rd param: name for accessing this path
    # info: <int:listing_id> is an parameter declaration
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
]