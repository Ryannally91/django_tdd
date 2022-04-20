from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('album/create', views.create), #remember not put the '/' in beginning
    path('album/<int:id>/edit', views.edit )
]
