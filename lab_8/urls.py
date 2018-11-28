from django.urls import re_path, path, include
from django.contrib import admin
from lab_8 import views as lab_8views

#url for app
urlpatterns = [
    re_path(r'^$', lab_8views.index),
    re_path('data', lab_8views.buku, name="buku"),
    path('admin/', admin.site.urls),
    path('subscribe/', include('Lab_10.urls')),
]
