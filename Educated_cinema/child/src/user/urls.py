from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='user/logout.html'), name='logout'),
] 