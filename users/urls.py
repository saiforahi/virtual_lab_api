from django.conf import settings
from django.contrib import admin
from django.urls import path
from .views import Login, Register, Logout,UserDetails


urlpatterns = [
    # path('api/logout/', Logout.as_view(), name='Logout'),
    path('login/', Login.as_view()),

    path('registration/', Register.as_view()),
    path('logout/', Logout.as_view()),
    path('details/', UserDetails.as_view()),
]