from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, AnonymousUser

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from .manager import CustomUserManager

# @csrf_exempt
@require_POST
def register_view(request):
    try:
        # Extract email and password from POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email and password are provided
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        # Create a new user using CustomUserManager
        user = CustomUser.objects.create_user(email=email, password=password)

        # If registration is successful, return success response
        return JsonResponse({'message': 'Registration successful', 'user_id': user.id})

    except ValueError as ve:
        # Handle validation errors
        return JsonResponse({'error': str(ve)}, status=400)
    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)}, status=500)

# @csrf_exempt
@require_POST
def login_view(request):
    try:
        # Extract email and password from POST request
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if email and password are provided
        if not email or not password:
            return JsonResponse({'error': 'Email and password are required'}, status=400)

        # Authenticate user
        user = authenticate(email=email, password=password)

        # Check if authentication was successful
        if user is not None:
            # Login the user
            login(request, user)
            userData = CustomUserManager.get_active_sessions(user)
            print(userData)
            return JsonResponse({'message': 'Login successful', 'user_id': user.id})
        else:
            # Authentication failed
            return JsonResponse({'error': 'Invalid email or password'}, status=400)

    except Exception as e:
        # Handle other exceptions
        return JsonResponse({'error': str(e)}, status=500)


# def check_login(request):
#     try:
#         if request.user.is_authenticated:
#             # User is logged in
#             message = "You are logged in as " + request.user.username
#         else:
#             # User is not logged in
#             message = "You are not logged in"
#         print(message)
#         return JsonResponse({"status": request.user.is_authenticated, "message": message})
#     except Exception as e:
#         # Handle any exceptions
#         return JsonResponse({"status": False, "message": "An error occurred: " + str(e)})
