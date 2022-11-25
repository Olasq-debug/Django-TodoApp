from django.urls import path 
from .views import CustomLoginView, UserRegister
from django.contrib.auth.views import LogoutView,PasswordResetView, PasswordResetDoneView
from django.urls import reverse_lazy 
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(template_name = 'user/Logout.html'), name = 'logout'),
    path('register/', UserRegister.as_view(), name = 'register'),
    path('password-reset/', PasswordResetView.as_view(template_name = 'user/password_reset.html'), name = 'password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(template_name ='user/password_resetdone.html'), name = 'password_reset_done'),
    
]