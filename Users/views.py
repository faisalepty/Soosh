from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def Signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Account successfuly created for {request.user}')
            user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
            if user != None:
                login(request, user)
                return redirect('Home')

    context = {'form': form}
    return render(request, 'signup.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')

        user = authenticate(username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('Home')
        else:
            messages.info(request, 'Username or Password is incorrect')
            return redirect('signup')

def Logout(request):
    logout(request)
    return redirect('signup')

