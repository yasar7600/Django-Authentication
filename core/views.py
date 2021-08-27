from django.shortcuts import render ,HttpResponseRedirect

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        return render(request, 'core/index.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/') 
