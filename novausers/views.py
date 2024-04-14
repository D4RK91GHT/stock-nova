import json
from django.contrib.auth import authenticate, login # type: ignore
from django.http import JsonResponse # type: ignore
from django.middleware.csrf import get_token # type: ignore
from .novaforms import UserRegistrationForm
from .models import RegisterUser

# ==================================================

def register(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            email = data.get('email', None)
            password = data.get('password', None)
        except json.JSONDecodeError:
            return JsonResponse({'status': 'false', 'message': 'Invalid JSON data'}, status=400)

        if email and password:
            # Check if the email already exists
            if RegisterUser.objects.filter(email=email).exists():
                return JsonResponse({'status': 'false', 'message': 'Email already exists'}, status=409)  # 409 Conflict
            else:
                form = UserRegistrationForm(data={'email': email, 'password': password})
                if form.is_valid():
                    form.save()
                    return JsonResponse({'status': 'true', 'message': 'User registered successfully'}, status=201)
                else:
                    return JsonResponse({'status': 'false', 'message': 'Invalid data provided'}, status=400)
        else:
            return JsonResponse({'status': 'false', 'message': 'Email and password are required fields'}, status=400)
    else:
        return JsonResponse({'status': 'false', 'message': 'Method not allowed'}, status=405)


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