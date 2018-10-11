from django.urls import re_path
from django.contrib import admin
from lab_6 import views as lab_6views

#url for app
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', lab_6views.profile),
    re_path(r'^delete/', lab_6views.DeleteStatus),
    re_path(r'^status/', lab_6views.addStatus),
]
