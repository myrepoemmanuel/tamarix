from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name="site-register"),
    path('profile/', views.profile, name="site-profile"),
    path('process_profile/', views.process_profile, name="process_profile"),
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="site-login"),
    path('login/',views.mylogin, name="site-login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name="site-logout"),
   
]