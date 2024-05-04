from django.urls import path
from . import views
from novauser.views import register_view, login_view



urlpatterns = [
    path('register/', register_view, name="tickers"),
    path('login/', login_view, name="tickers"),
    path('tickers/', views.tickerList, name="tickers"),
    path('showdata/', views.showdata, name='showdata'),
    path('cstoken/', views.get_csrf_token, name='showdata'),


    
]
