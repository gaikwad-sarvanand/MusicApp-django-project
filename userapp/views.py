from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewCreateForm
# Create your views here.


def indexpage(request):
    return render(request, "index.html")


def registration_request(request):
    if request.method == 'POST':
        form = NewCreateForm(request.POST)
        if form.is_valid():
            form.save()
            # username = form.cleaned_data['username']
            # password = form.cleaned_data['password1']
            # user = authenticate(username=username, password=password)
            # login(request, user)
            messages.success(request, ("Registration SuccessFull!"))
            return redirect('/')
    else:
        form = NewCreateForm()
    return render(request, "register.html", {'form': form})


def homepage(request):
    return render(request, "home.html")


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, ("You're Logged In right now!"))
            # Redirect to a success page.
            return redirect('/home_page')
        else:
            # Return an 'invalid login' error message.
            messages.success(
                request, ("There was a Error loging In,Try Again!"))
            return redirect('/login_user')
    else:
        return render(request, 'login.html', {})


def logout_user(request):
    logout(request)
    messages.success(
        request, ("You were Logged Out!"))
    return redirect('/')
