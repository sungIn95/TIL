"""practive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from numver import views

urlpatterns = [
    path("", views.index),
    path("admin/", admin.site.urls),
    path("is-odd-even/<int:number>", views.is_odd_even),
    path("is-odd-even/", views.is_odd_even_alert),
    path("calculate/<int:number>/<int:number2>", views.calculate),
    path("previous-life", views.previous_life),
    path("previous-life/check", views.previous_life_check),
    path("lipsum", views.lipsum),
    path("lipsum/check", views.lipsum_check),
    #
]
