from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('random', views.random),
    path('handle_random', views.handle_random),
    path('reset_random', views.reset_random)
]