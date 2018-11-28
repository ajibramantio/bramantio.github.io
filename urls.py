from django.urls import path, include
from .views import subscribe, checkEmail
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', subscribe, name="subscribe"),
   
   
]
