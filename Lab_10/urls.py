from django.urls import path, include
from .views import subscribe, checkEmail, subs_list_json, unsubscribe
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', subscribe, name="subscribe"),
    path('checkEmail/', checkEmail, name="checkEmail"),
    path('get-subs-list/', subs_list_json),
    path('subscribe/delete/', unsubscribe),

]
