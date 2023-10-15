"""
URL configuration for iot project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from randw import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name = 'home'),
    path('about/', views.about,name = 'about'),
    path('user/', views.user,name = 'user'),
    path('police/', views.police,name = 'police'),
    path('hospital/', views.hospital,name = 'hospital'),
    path('service/',views.service,name = 'service'),
    path('Registration/',views.registration, name = 'registration' ),
    path('login/',views.login_view, name = 'login'),
    path('iotdata/',views.iotdata,name = 'iotdata'),
    path('logout/', views.logout_view, name='logout'),
    path('violationlist', views.violationlist, name='vlist'),
    path('ownerdetails/', views.ownerdetails, name='ownerdetails'),
    path('regiscert/', views.registrationcert, name='regiscert'),
    path('insurance/', views.insurance, name='insurance'),

]

