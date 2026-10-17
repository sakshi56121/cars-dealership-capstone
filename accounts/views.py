import json
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

@csrf_exempt
@require_POST
def login_user(request):
    try:
        data = json.loads(request.body)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return JsonResponse({"error": "Invalid JSON request body."}, status=400)

    user = authenticate(
        request,
        username=data.get("username", ""),
        password=data.get("password", ""),
    )

    if user is None:
        return JsonResponse({"error": "Invalid username or password."}, status=401)

    login(request, user)
    return JsonResponse({
        "message": "Login successful.",
        "username": user.get_username(),
    })

@csrf_exempt
@require_POST
def logout_user(request):
    if not request.user.is_authenticated:
        return JsonResponse({"error": "User is not logged in."}, status=401)

    logout(request)
    return JsonResponse({"message": "Logout successful."})
