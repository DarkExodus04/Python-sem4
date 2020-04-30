
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from mainapp.models import Hackathons,Cities
from mainapp.Scraper import Webhack


@login_required(login_url="mainapp:login")
def home(request):
    # w = Webhack()
    # w.cities()
    cities = Cities.objects.all()
    return render(request,'mainapp/home.html',{'cities':cities})


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
    if request.method == 'GET':
        logout(request)
        return redirect("mainapp:home")

def view_hack(request,city):
    cityview = Cities.objects.get(city = str(city))
    hackathons = Hackathons.objects.filter(city_id = cityview.id)
    return render(request, 'mainapp/hackathons.html', {'hackathons': hackathons, 'city': city})

def scrape(request):
    w = Webhack()
    # w.cities()
    Hackathons.objects.all().delete()
    cities = Cities.objects.all()
    for city in cities:
        w.webhackathons(city,city.id)
    return redirect("mainapp:home", permanent= True)
