from django.shortcuts import render ,HttpResponseRedirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm , PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout , update_session_auth_hash

# Create your views here.

#for signup user
def sign_up(request):
    if request.method == 'POST':
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Your Accout is Successfuly Created!!')
            fm.save()
            # uname = fm.cleaned_data['username']
            # upass = fm.cleaned_data['password']
            # reg = UserCreationForm(username= uname, password= upass)
            # reg.save()
            #return HttpResponseRedirect('/login/')
    else:
        fm = SignUpForm()
    return render(request, 'authLS/signup.html',{'form': fm})



#for login user
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username= uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,"Logged in Successfully")
                    return HttpResponseRedirect('/')
        else:
            fm = AuthenticationForm()
        return render(request, 'authLS/login.html',{"form": fm}) 
    else:
        return HttpResponseRedirect('/')



#for logout user
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/login/')


#password change with old password
def password_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,"Password Change Successfully !!!")
                return HttpResponseRedirect('/')
        else:    
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'authLS/passwordchange.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')


#password change without old password
def password2_change(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = SetPasswordForm(user=request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request, fm.user)
                messages.success(request,"Password Change Successfully !!!")
                return HttpResponseRedirect('/')
        else:    
            fm = SetPasswordForm(user=request.user)
        return render(request, 'authLS/passwordchange.html',{'form':fm})
    else:
        return HttpResponseRedirect('/login/')