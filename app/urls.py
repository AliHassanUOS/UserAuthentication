from django.urls import path
from .import views



urlpatterns = [

    path("",views.formshow,name="home"),
    path('login/',views.loginform, name = "login"),
    path('profile/',views.profileform,name='profile'),
    path("logout/",views.user_logout,name='logout'),
    path('passwordchange/',views.password_change, name="password")
    
    
]
