from django.urls import path 
from .views import signup, dashboard



urlpatterns = [
    path('signup' , signup),
    path('dashboard' , dashboard),
]