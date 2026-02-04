from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from django.views.generic import RedirectView


urlpatterns = [
    path("", RedirectView.as_view(url="/api/v1/auth/register-page/", permanent=False)),
    path("admin/", admin.site.urls),

    path("api/v1/auth/", include("accounts.urls")),
    path("api/v1/auth/refresh/", TokenRefreshView.as_view()),

    path("api/v1/", include("tasks.urls")),
]
