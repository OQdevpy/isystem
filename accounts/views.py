from pprint import pprint 
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required


# Create your views here.

# 1-usul login tayyor narsdan foydalanmasdan
def _login_view(request):
      query_dict=request.POST
      username=query_dict.get('username')
      password=query_dict.get('password')
      if request.method == 'POST':
            user=authenticate(request,username=username,password=password)
            if user is None:
                  context={'error':'Invalid username or password'}
                  return render(request, 'accounts/login.html', context)

            login(request,user)
            return redirect('/')

      return render(request, 'accounts/login.html')


# 2-usul login tayyor narsdan foydalanib yani        from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
def login_view(request):
      form=AuthenticationForm(request)
      if request.method == 'POST':
            form=AuthenticationForm(request,data=request.POST)
            if form.is_valid():
                  user=form.get_user()
                  login(request,user)
                  return redirect('/')
      return render(request, 'accounts/login.html',{'form':form})

@login_required()
def logout_view(request):
      if request.method == 'POST':
            logout(request)
            return redirect('accounts:login')

      return render(request, 'accounts/logout.html')

def signup_view(request):
      form=SignUpForm(request.POST or None)
      if request.method == 'POST':
            if form.is_valid():
                  form.save()
                  return redirect('accounts:login')
      context={'form': form}
      return render(request, 'accounts/signup.html',context)