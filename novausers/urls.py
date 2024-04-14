from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name="tickers"),
    # path('login/', views.userLogin, name="tickers"),
]
