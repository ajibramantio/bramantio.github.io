from django.urls import re_path, path
from django.conf.urls import url, include
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.http import HttpResponse
from django.contrib import admin
from lab_8 import views as views

#url for app
urlpatterns = [
    re_path(r'^$', views.index),
    re_path('data', views.buku, name="buku"),
    path('admin/', admin.site.urls),
    path('subscribe/', include('Lab_10.urls')),
    path('log/', views.login, name='log'),
    url(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    url(r'^auth/$', include('social_django.urls', namespace='social'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
]
