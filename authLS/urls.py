from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/',views.sign_up,name = 'signup'),
    path('login/',views.log_in,name = 'login'),
    path('logout/',views.log_out,name = 'logout'),
    path('passwordchange/',views.password_change,name = 'passwordchange'),
    path('password2change/',views.password2_change,name = 'password2change'),
]