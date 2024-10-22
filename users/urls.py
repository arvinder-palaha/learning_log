'''Defines URL patterns for users.'''

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # include default auth urls
    path('', include('django.contrib.auth.urls')),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
]
