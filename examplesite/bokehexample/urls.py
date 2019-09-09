from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('<str:id>/', views.url_pattern_test, name='url_pattern_test'),
]
