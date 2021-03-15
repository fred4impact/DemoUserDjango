from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from accounts.forms import UserRegisterForm
from django.contrib import messages




def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            # name =form.cleaned_data.get('name')
            # city = form.clean.data.get('city') 
            # messages.success(request, f'Account created for {username}!')

            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('/')
          
    else:
       form = UserRegisterForm()
    return render(request,'account/register.html', {'form': form })       


