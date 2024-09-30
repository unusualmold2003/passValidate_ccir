from django.shortcuts import render
from django.http import HttpResponse

def password_validator(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if validate_password(password):
            return HttpResponse("Password is valid")
        else:
            return HttpResponse("Password is invalid")
    return render(request, 'password_validator.html')

def validate_password(password):
    password = request.GET.get('password', '')
    result = zxcvbn(password)
    return JsonResponse(result)
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isalpha() for char in password):
        return False
    return True

