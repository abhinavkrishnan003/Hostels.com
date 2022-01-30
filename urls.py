"""dothack2022_project URL Configuration

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
from . import contents

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contents.page1),
    path('index.html', contents.page1),
    path('Beauxbatons.html', contents.page2),
    path('Hogwarts.html', contents.page3),
    path('girlsbeauxbatons.html', contents.page4),
    path('boysbeauxbatons.html', contents.page5),
    path('girlshogwarts.html', contents.page6),
    path('boyshogwarts.html', contents.page7),
    path('hostel1.html', contents.page8),
    path('hostel2.html', contents.page9),
    path('forms.html', contents.page10),
    path('thanks.html', contents.page11),
]
