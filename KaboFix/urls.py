"""KaboFix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from KaboFixApp.views import main_page, KaboLogin_page, KaboRegister_page, KaboLogout_page, KaboWrite_Page, KaboRead_Page, Kabo_MainAdmin_Page, Kabo_ReadAdmin_Page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('login/', KaboLogin_page),
    path('logout', KaboLogout_page),
    path('register/', KaboRegister_page),
    path('write/', KaboWrite_Page),
    path('read/', KaboRead_Page),

    path('mainadmin/', Kabo_MainAdmin_Page),
    path('readadmin/', Kabo_ReadAdmin_Page),
]

