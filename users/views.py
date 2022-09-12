from django.shortcuts import render


def register(request):
    return render(request, 'users/registration.html')
# Create your views here.
