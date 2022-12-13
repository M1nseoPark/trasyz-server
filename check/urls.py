from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index),
    path('', views.IndexView.as_view(), name='index'),
]