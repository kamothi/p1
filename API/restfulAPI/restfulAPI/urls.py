from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from dataTest import views
# Serializers define the API representation.

urlpatterns = [
    path('users/', views.user_list),
    path('login/',views.login),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('sign/',views.signup),
    path('check/',views.check_login),
    path('board/', views.board_list),
]