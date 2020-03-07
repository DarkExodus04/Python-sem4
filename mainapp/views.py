from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required

@login_required(login_url="mainapp:login")
def home(request):
    return render(request,'mainapp/home.html')


def register_view(request):
    if request.method == 'POST' :
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect("mainapp:home")
    else:
        form = UserCreationForm()
    return render(request, 'mainapp/register.html', {'form':form})

def login_view(request):
    if request.method == "POST" :
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect("mainapp:home")
    else:
        form = AuthenticationForm()
    return render(request,"mainapp/login.html",{'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect("mainapp:home")

