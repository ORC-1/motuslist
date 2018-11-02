"""MTL_LISTING URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from listing.views import (HomeView,
                            search,
                            Travel,
                            Art,
                            Book_Shop,
                            Restaurants,
                            Business
                            )
from django.contrib import admin
from django.urls import path, include
from django.conf import settings #Added for video not found error TroubleShooting 24.05.2018 --No Effect
admin.site.site_header = 'Motus Listing|Admin'
admin.site.site_title = 'Motus admin'
from listing.apiviews import SearchResult


urlpatterns = [
    path("apisearch/", SearchResult.as_view(), name="apisearch"),
    path('', HomeView.as_view(), name='home'),
    path('hitcount/', include('hitcount.urls', namespace='hitcount')),
    path('search/', search, name='search'),
    path('travel', Travel.as_view(), name="travel"),
    path('art',Art.as_view() , name='art'),
    path('book',Book_Shop.as_view() , name='book'),
    path('restaurants',Restaurants.as_view() , name='restaurants'),
    path('business',Business.as_view() , name='business'),
    path('admin/', admin.site.urls),
]
