from django.urls import path

from .views import Home, QuestionAdd, CommentAdd, Like, Hashtag, Questions, Search

urlpatterns = [
    path('', Home, name='Home'),
    path('add_question/',QuestionAdd, name='QuestionAdd'),
    path('quests/', Questions, name='Questions'),
    path('search/', Search, name='Search'),
    path('add_comment/<int:question_id>/', CommentAdd, name='CommentAdd'),
    path('like/<int:pk>/',Like, name='Like'),
    path('hashtag/<str:hashtag>/',Hashtag, name='Hashtag'),
]