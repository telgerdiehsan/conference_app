from django.urls import path,include
from api import views

urlpatterns = [
    path('hello/',views.index,name='index'),
    path('login',views.googleLogin.as_view()),
    path('create-room',views.Room.as_view())
] 