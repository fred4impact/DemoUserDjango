from django.shortcuts import render
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def courier(request):
    return render(request, 'courier/courier.html')