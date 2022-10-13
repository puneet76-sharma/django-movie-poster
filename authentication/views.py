from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm, SetPasswordForm, UserChangeForm
from .forms import ProfileEditForm, ProfileAdminEditForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User


# Create your views here.

def index(request):
    return render(request, 'index.html')

def sign_up(request):

    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST) # By default only showing 3 fields- username, password, Password confirmation
        if form.is_valid():
            messages.success(request, 'Account Created Successfully')
            form.save()
    return render(request, 'signup.html', {'form':form})


def user_login(request):
    if not request.user.is_authenticated:
        form=AuthenticationForm()
        if request.method=='POST':
            form=AuthenticationForm(request=request, data= request.POST) # In AuthenticationForm post request, we need to gives two parameters
            if form.is_valid():
                username=form.cleaned_data['username']
                password=form.cleaned_data['password']

                user= authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Your Account is Login!!!')
                return HttpResponseRedirect('/auth/profile/')
        return render(request, 'login.html', {'form':form})
    else:
        return HttpResponseRedirect('/auth/profile/')


def user_profile(request):
    if request.user.is_authenticated:
        if request.user.is_superuser==False:
            form= ProfileEditForm(instance=request.user)
            obj=None
        else:
            form=ProfileAdminEditForm(instance=request.user)
            obj=User.objects.all()
        if request.method=='POST':
            form=ProfileEditForm(instance=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User Update Successfully')
                return HttpResponseRedirect('/auth/profile/')

        return render(request, 'profile.html', {'name':request.user,'form':form, 'obj':obj})
    else:
        return HttpResponseRedirect('/auth/signup/')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/auth/login/')

    
def user_details(request, id):
    if request.user.is_authenticated:
        obj=User.objects.get(pk=id)
        form=ProfileAdminEditForm(instance=obj)
        if request.method=='POST':
            form=ProfileAdminEditForm(instance=obj, data=request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'User Profile Saved Successfully')

                return HttpResponseRedirect(request.META.get('HTTP_REFERER')) # This is for return same page where you are

        return render(request, 'user-details.html', {'name':request.user, 'form':form})
    else:
        return HttpResponseRedirect('/auth/login/')