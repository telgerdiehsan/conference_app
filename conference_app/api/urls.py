from django.urls import path,include
from api import views

urlpatterns = [
    path('login',views.googleLogin.as_view())
] 