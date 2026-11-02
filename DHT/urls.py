from django.urls import path
from .views import coucou
urlpatterns = [
    path('coucou/', coucou, name='coucou'),
    
]