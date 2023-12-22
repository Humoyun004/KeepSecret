from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup, ProfileInfo, Logout, ProfileUpdate

urlpatterns = [
    path('register/', signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='Login'),
    path('profile/', ProfileInfo, name='ProfileInfo'),
    path('logout/', Logout, name='Logout'),
    path('profile/update/', ProfileUpdate, name='ProfileUpdate')
]