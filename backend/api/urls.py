from django.urls import path
from . import views

urlpatterns = [
    path('boardgames/', views.BoardgameList.as_view(), name='boardgame-list'),
    path('stats/', views.StatsList.as_view(), name='stats-list'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('', views.api_root),
]
