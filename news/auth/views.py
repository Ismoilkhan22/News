from django.shortcuts import render


def login(request):
    return render(request, "auth/login.hmtl")


def regis(request):
    return render(request, "auth/register.hmtl")


def logout(request):
    return render(request, "auth/logout.hmtl")
