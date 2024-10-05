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
    path('logout', wallet_views.login, name="logout"),
    path('movements/', wallet_views.movements, name='movements'),
    path('data_form/', wallet_views.data_form, name='dataaform'),
    #path('categories/', wallet_views.categories, name='categories'),
    path('categories/', wallet_views.categoria_list, name='categoria_list'),  # Nueva URL para listar categorías
    path('categories/create/', wallet_views.categoria_create, name='categoria_create'),  # URL para crear categoría
    path('categories/update/<int:pk>/', wallet_views.categoria_update, name='categoria_update'),  # URL para actualizar categoría
    path('categories/delete/<int:pk>/', wallet_views.categoria_delete, name='categoria_delete'),  # URL para borrar categoría
    path('statistics/', wallet_views.statistics, name='statistics'),
    path('suggestions/', wallet_views.suggestions, name='suggestions'),
    path('goals/', wallet_views.goals, name='goals'),
    path('events/', wallet_views.events, name='events'),
]