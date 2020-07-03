from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']  # same as the name in the HTML file
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            # writing to database, user model object is already in django;
            if User.objects.filter(username=username).exists():
                # print('Username already taken.')
                messages.info(request, 'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already taken.')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name, last_name=last_name)
                user.save()
                return redirect('login')  # redirects to the home-page
        else:
            messages.info(request, 'Password mismatch')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')  # this will be executed on get request


def logout(request):
    auth.logout(request)
    return redirect('/')