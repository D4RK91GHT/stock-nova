from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, AnonymousUser

from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from .models import CustomUser, Wishlist
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
    if request.method == "POST":
        try:
            # Extract email and password from POST request
            email = request.POST.get('email')
            password = request.POST.get('password')

            # Check if email and password are provided
            if not email or not password:
                return JsonResponse({'status': False, 'message': 'Email and password are required'})

            # Authenticate user
            user = authenticate(email=email, password=password)

            # Check if authentication was successful
            if user is not None:
                # Login the user
                login(request, user)
                return JsonResponse({'status': True, 'message': 'Login successful', 'user_id': user.id})
            else:
                # Authentication failed
                return JsonResponse({'status': False, 'message': 'Invalid email or password'})

        except Exception as e:
            # Handle other exceptions
            return JsonResponse({'status': False, 'error': str(e)})
    else:
        return JsonResponse({'status': False,'message': 'Request method is not allow!'})


@login_required
def check_login(request):
    try:
        if request.user.is_authenticated:
            # User is logged in
            message = "You are logged in as " + request.user.email
        else:
            # User is not logged in
            message = "You are not logged in"
        return JsonResponse({"status": True, "message": message})
    except Exception as e:
        # Handle any exceptions
        return JsonResponse({"status": False, "message": "An error occurred: " + str(e)})
    

def logout_view(request):
    logout(request)
    # Redirect to a page after logout, for example, the homepage
    return JsonResponse({"status": True, "message": "Logged Out Sucessfully!"})
    



@login_required
def add_to_wishlist(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        user = request.user
        Wishlist.objects.add_to_wishlist(ticker=ticker, user=user)
        return JsonResponse({'status': True})
    return JsonResponse({'status': False})


@login_required
def remove_from_wishlist(request):
    if request.method == 'POST':
        ticker = request.POST.get('ticker')
        user = request.user
        success = Wishlist.objects.remove_from_wishlist(ticker=ticker, user=user)
        return JsonResponse({'status': success})
    return JsonResponse({'status': False})