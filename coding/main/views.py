from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.contrib import messages



def index(request:HttpRequest):
    if request.method == "POST":
        password = request.POST.get("password")
        if validate_password(password):
            messages.success(request, "Your password strength is GOOD")
        else:
            messages.success(request, "Ah! Please try a new password as it's not secure")
    return render(request, "main/index.html")

    
def validate_password(password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True



    
