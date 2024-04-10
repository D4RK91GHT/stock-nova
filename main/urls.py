from django.urls import path
from . import views


urlpatterns = [
    path('tickers/', views.tickerList, name="tickers"),
    path('showdata/', views.showdata, name='showdata'),
    path('cstoken/', views.get_csrf_token, name='showdata'),


    
]
