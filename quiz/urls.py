from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('setup/', views.quiz_setup, name='quiz_setup'),
    path('quiz/', views.start_quiz, name='start_quiz'),
    path('result/', views.result, name='result'),
]
