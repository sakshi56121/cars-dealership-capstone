import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST


def authenticate_request(request, username_key):
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return None, JsonResponse(
            {"error": "Invalid JSON request body."}, status=400
        )

    username = data.get(username_key, "")
    password = data.get("password", "")

    user = authenticate(
        request, username=username, password=password
    )

    if user is None:
        return None, JsonResponse(
            {"error": "Invalid username or password."}, status=401
        )

    return user, None


@csrf_exempt
@require_POST
def login_user(request):
    user, error = authenticate_request(request, "username")
    if error:
        return error

    login(request, user)
    return JsonResponse({
        "message": "Login successful.",
        "username": user.get_username(),
    })


@csrf_exempt
@require_POST
def djangoapp_login(request):
    user, error = authenticate_request(request, "userName")
    if error:
        return error

    login(request, user)
    return JsonResponse({
        "status": "Authenticated",
        "userName": user.get_username(),
    })


@csrf_exempt
@require_POST
def logout_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User is not logged in."}, status=401)

    username = request.user.get_username()
    logout(request)
    return JsonResponse({"userName": ""})
