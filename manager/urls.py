from django.urls import path
from . import views

# http://127.0.0.1:8000/manager/rent/?pid=1&mid=1&latitude=1&longitude=1

app_name = 'manager'
urlpatterns = [
    path('', views.index),
    # http://도메인/manager/?id=123 같은 요청이 들어온 경우 get_post 함수로 파라미터 전달
    path('rent/', views.get_post),
]