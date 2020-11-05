"""QuestionTime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView
from users.forms import CustomUserForm
from core.views import indexTemplateView

urlpatterns = [

    # Django Admin panel
    path('admin/',
         admin.site.urls),

    # Login with Browsable API
    path('api-auth/',
         include('rest_framework.urls')),

    # Login with REST Framework (rest_auth)
    path('api/rest-auth/',
         include('rest_auth.urls')),

    # Registration with REST Framework (rest_auth)
    path('api/rest-auth/registration/',
         include('rest_auth.registration.urls')),

    # Login from browser with Django standard views
    path('accounts/',
         include('django.contrib.auth.urls')),

    # Registration from browser with Django-registration views
    path('accounts/register/',
         RegistrationView.as_view(
             form_class=CustomUserForm,
             success_url="/"),
         name='django_register_registration'),

    # Urls for browser with Django-registration views
    path('accounts/register/',
         include('django_registration.backends.one_step.urls')),

    # Custom users REST API
    path('api/',
         include('users.api.urls')),

    path('api/',
         include('questions.api.urls')),

    # Index page redirect
    re_path(r"^.*$",
            indexTemplateView.as_view(),
            name="entry_point")

]
