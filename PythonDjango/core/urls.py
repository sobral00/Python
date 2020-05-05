from django.urls import path, include
from .views import home

urlpatterns = [
    path('core/', home, name='core_home')
]
