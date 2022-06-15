from django.urls import path
from .views import *

app_name = 'todoapp'

urlpatterns = [
    path('', home, name='home'),
    path('single/<int:pk>/', single, name='single'),
    path('delete/<int:pk>/', delete, name='delete'),
    path('create/', create, name='create'),
]
