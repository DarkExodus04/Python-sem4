from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('', views.home, name = "home"),
    path('login/',views.login_view, name = "login"),
    path('logout/', views.logout_view, name = "logout"),
    path('register/', views.register_view, name = "register"),
    path('scrape/', views.scrape, name="scrape"),
    path('<str:city>/',views.view_hack, name = "hackathon"),
]