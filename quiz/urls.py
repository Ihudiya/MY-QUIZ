from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('start/<slug:topic_slug>/', views.start_quiz, name='start_quiz'),
    path('results/', views.quiz_results, name='quiz_results'),
    path('next-round/', views.next_round, name='next_round'),
]