from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
urlpatterns = [
  path('', views.home, name='home'),
  path('story/<int:Cinema_id>/', views.Cinema_detail, name='detail'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)