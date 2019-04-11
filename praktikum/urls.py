"""Lab1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.urls import re_path
from django.contrib import admin
from lab_4.views import index as lab_4
from lab_6.views import index as lab_6
from lab_8.views import index as lab_8
from Lab_10.views import subscribe as Lab_10
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^lab-1/', include('lab_1.urls')),
    re_path(r'^lab-2/', include('lab_2.urls')),
    re_path(r'^lab-8/', lab_8, name='index'),
    re_path(r'^$', include('lab_4.urls'), name='HomePage'),
    re_path(r'^lab-6/', include('lab_6.urls'), name='lab-6'),
    # re_path(r'^lab-8/', include('lab_8.urls'), name='lab-8'),
    # path('', include('lab_8.urls')),
    re_path('Lab_10/', include('Lab_10.urls'), name='Lab_10'),
    re_path('lab11/', include('lab11.urls')),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
]
