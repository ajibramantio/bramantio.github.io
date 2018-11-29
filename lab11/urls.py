from django.contrib import admin
from django.urls import path, include
from . import views as lab11
from django.contrib.auth import views
from django.conf import settings


urlpatterns = [
    path('', lab11.indexlab11, name='indexlab11'),
    path('book-list/', lab11.index, name='indexlab9'),
    path('book-list/json/', lab11.booklist, name='books-list'),
    path('login/',  views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('auth/', include('social_django.urls', namespace='social')),
    path('book-list/like/', lab11.like),
    path('book-list/unlike/', lab11.unlike),
    path('book-list/get-like/', lab11.get_like),
]