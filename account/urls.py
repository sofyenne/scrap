from django.urls import path
from .import views


urlpatterns = [

    path('login/', views.Login , name='login' ),
    path('register/' , views.register , name='register'),

    path('logout/' , views.Logout , name='logout')

]