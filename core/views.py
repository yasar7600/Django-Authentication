from django.shortcuts import render ,HttpResponseRedirect
#from django.contrib.auth.forms import UserChangeForm
from django.contrib import messages
from .forms import EditUserProfile

# Create your views here.

def index(request):
    if request.user.is_authenticated:
       # fm = UserChangeForm(instance=request.user)
        if request.method == "POST":
            fm = EditUserProfile(request.POST,instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request,"Profile Updated !!!")

        else:
            fm = EditUserProfile(instance=request.user)
        return render(request, 'core/index.html', {'name': request.user,'form':fm})
    else:
        return HttpResponseRedirect('/login/') 
