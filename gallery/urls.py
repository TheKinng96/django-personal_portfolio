from django.urls import path, include
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.all_photos, name='all_photos'),
    path('<int:photo_id>/', views.gallery, name='gallery'),
]
