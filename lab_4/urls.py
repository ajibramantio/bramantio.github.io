from django.urls import re_path
from .views import index, addschedule, schedule, InputForm, DeleteSched
from django.contrib import admin

#url for app
urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', index, name="index"),
    re_path(r'^addSchedule/', InputForm, name="addschedule"),
    re_path(r'^Schedules/', schedule, name="schedule"),
    re_path(r'^adding/', addschedule, name="adding"),
    re_path(r'^delete/', DeleteSched, name='DeleteSched')
]
