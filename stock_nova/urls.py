"""
URL configuration for stock_nova project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from novauser.views import *
from main.views import *

urlpatterns = [



    path('register/', register_view, name="tickers"),
    path('login/', login_view, name="login"),
    path('checklogin/', check_login, name="check_login"),
    path('logout/', logout_view, name="logout"),

    path('addwish/', add_to_wishlist, name="addwish"),
    path('removeWish/', remove_from_wishlist, name="removeWish"),
       
    path('tickers/', tickerList, name="tickers"),
    path('current/', marketChart, name="marketChart"),
    path('showdata/', showdata, name='showdata'),
    path('predicted-graph/', predictedGraphOnly, name='Predicted Graph'),


    
    # path('cstoken/', get_csrf_token, name='showdata'),

    path('admin/', admin.site.urls),
]
