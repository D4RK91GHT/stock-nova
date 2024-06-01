import json
from django.contrib.auth import authenticate, login, logout # type: ignore
from django.http import JsonResponse # type: ignore
from django.middleware.csrf import get_token # type: ignore
from .data import *
from .models import *
from django.contrib.auth import get_user_model # type: ignore
# from ..novausers.novaforms import UserRegistrationForm
# from .models import RegisterUser

User = get_user_model()

# ==================================================

# def register(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             email = data.get('email', None)
#             password = data.get('password', None)
#         except json.JSONDecodeError:
#             return JsonResponse({'status': 'false', 'message': 'Invalid JSON data'}, status=400)

#         if email and password:
#             # Check if the email already exists
#             if RegisterUser.objects.filter(email=email).exists():
#                 return JsonResponse({'status': 'false', 'message': 'Email already exists'}, status=409)  # 409 Conflict
#             else:
#                 form = UserRegistrationForm(data={'email': email, 'password': password})
#                 if form.is_valid():
#                     form.save()
#                     return JsonResponse({'status': 'true', 'message': 'User registered successfully'}, status=201)
#                 else:
#                     return JsonResponse({'status': 'false', 'message': 'Invalid data provided'}, status=400)
#         else:
#             return JsonResponse({'status': 'false', 'message': 'Email and password are required fields'}, status=400)
#     else:
#         return JsonResponse({'status': 'false', 'message': 'Method not allowed'}, status=405)


# ==================================================

# def userLogin(request):
#     if request.method == 'POST':
#         data = request.POST  # Assuming you're sending form data via POST
#         email = data.get('email', None)
#         password = data.get('password', None)
#         print(email)
#         print(password)


#         if email and password:
#             user = authenticate(request, email=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return JsonResponse({'status': 'true', 'message': 'Login successful'})
#             else:
#                 return JsonResponse({'status': 'false', 'message': 'Invalid email or password'}, status=400)
#         else:
#             return JsonResponse({'status': 'false', 'message': 'Email and password are required fields'}, status=400)
#     else:
#         return JsonResponse({'status': 'false', 'message': 'Method not allowed'}, status=405)

# ==================================================

def tickerList(request):
    allTickers = nse_list()
    return JsonResponse({"tickers": allTickers}, safe=False)

# ==================================================

def marketChart(request):
    try:
        if request.method == "POST":
            symbol = request.POST.get('symbol')
            response_data = currentMarket(symbol)

            return JsonResponse(response_data)
        else:
            errcontext = {'custom_message': 'Nothing Passed'}
            return JsonResponse(errcontext)
    except Exception as e:
        # Catch any exceptions and return an empty JSON response or handle it appropriately
        return JsonResponse({'error': str(e)}, status=500)
# ==================================================


def showdata(request):
    try:
        if request.method == "POST":
            symbol = request.POST.get('symbol')
            period = request.POST.get('period')

            response_data = predections(symbol, days=period)
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


def predictedGraphOnly(request):
    try:
        if request.method == "POST":
            symbol = request.POST.get('symbol')
            period = request.POST.get('period')

            response_data = predictedGraph(symbol, days=period)
            return JsonResponse(response_data)
        else:
            errcontext = {
                'custom_message': 'Nothing Passed'
            }
            return JsonResponse(errcontext, safe=False)
    except Exception as e:
        # Catch any exceptions and return an empty JSON response or handle it appropriately
        return JsonResponse({'error': str(e)}, status=500)

# ===================================================
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({'csrfToken': token})
