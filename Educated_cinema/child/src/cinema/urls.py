
from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('detail/<int:Cinema_id>/', views.Cinema_detail, name='detail'),
]


