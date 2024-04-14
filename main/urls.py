from django.urls import path
from . import views


urlpatterns = [
    # path('register/', views.register, name="tickers"),
    # path('login/', views.userLogin, name="tickers"),
    path('tickers/', views.tickerList, name="tickers"),
    path('showdata/', views.showdata, name='showdata'),
    path('cstoken/', views.get_csrf_token, name='showdata'),


    
]
