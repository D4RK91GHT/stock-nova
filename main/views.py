from django.shortcuts import render,redirect
from django.http import JsonResponse
import base64
from datetime import date
from io import BytesIO
from prophet import Prophet
from prophet.plot import plot_plotly
import matplotlib.pyplot as plt
from main.models import RawData,ChartGraphs
from django.middleware.csrf import get_token

from .serializers import StockListSerializer
from rest_framework.generics import ListAPIView

from .data import allTickers, predections

# ==================================================

def tickerList(request):
    return JsonResponse(allTickers, safe=False)

# ==================================================

def showdata(request):
    try:
        if request.method == "POST":
            symbol = request.POST.get('symbol')
            response_data = predections(symbol)
            return JsonResponse(response_data)
        else:
            errcontext = {
                'custom_message': 'Nothing Passed'
            }
            return JsonResponse(errcontext)
    except Exception as e:
        # Catch any exceptions and return an empty JSON response or handle it appropriately
        return JsonResponse({'error': str(e)}, status=500)

# ===================================================


def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})
