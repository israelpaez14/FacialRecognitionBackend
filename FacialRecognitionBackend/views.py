import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_endpoint(request):
    if request.method != "POST":
        return HttpResponse("Not supported Method", status=405)

    try:
        body = json.loads(request.body)
        user = authenticate(request, username=body["username"], password=body["password"])
        if user is None:
            return JsonResponse({"error": "Invalid credentials"}, status=403, safe=False)
        login(request, user)
        print(user)
        return JsonResponse({"detail": "Login Successful"}, safe=True, status=200)

    except Exception as ex:
        return JsonResponse({"error": "Bad request"}, status=400, safe=False)


def logout_endpoint(request):
    if request.method != "GET":
        return HttpResponse("Not supported method", status=405)

    logout(request)

    return HttpResponse("Logged out")


@login_required
def main(requst):
    return HttpResponse("Its working")
