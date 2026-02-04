from django.urls import path
from .views import RegisterView, LoginView

from .views import (RegisterView,LoginView,register_page,login_page,dashboard_page,)


urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]




urlpatterns = [
    
    path("register/", RegisterView.as_view()),
    path("login/", LoginView.as_view()),

    
    path("register-page/", register_page),
    path("login-page/", login_page),
    path("dashboard/", dashboard_page),
]
