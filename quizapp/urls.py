from django.urls import path, include
from quizapp import views


urlpatterns = [
    path('index/', views.index, name='index'),
    path('quiz/<id>/<email>', views.quiz, name='quiz'),
    path('dashboard/<score>', views.dashboard, name='dashboard'),
    path('show/<exam_id>', views.showuser, name='showuser')
]
