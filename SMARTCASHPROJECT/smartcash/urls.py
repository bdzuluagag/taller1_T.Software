"""smartcash URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from wallet import views as wallet_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', wallet_views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('register/', wallet_views.register, name="register"),
    path('movements/', wallet_views.movements, name='movements'),
    path('data_form/', wallet_views.data_form, name='dataaform'),
    path('categories/', wallet_views.categories, name='categories'),
    path('statistics/', wallet_views.statistics, name='statistics'),
    path('suggestions/', wallet_views.suggestions, name='suggestions'),
]
