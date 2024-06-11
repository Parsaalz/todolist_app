from django.urls import path
from . import views
urlpatterns=[
    path('signup/',views.signuppage,name="signuppage"),
    path('login/',views.loginpage,name="loginpage"),
    path('logout/',views.logoutpage,name="logoutpage"),
]