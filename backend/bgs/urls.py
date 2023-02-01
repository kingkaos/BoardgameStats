from django.urls import path
from . import views

urlpatterns = [
    path('boardgames/', views.BoardgameList.as_view(), name='boardgame-list'),
    path('', views.api_root),
]
