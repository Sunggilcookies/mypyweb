from django.urls import path
from . import views

app_name = 'board'




urlpatterns = [
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('question/create/', views.question_create,
         name='question_create'), #질문등록
    path('answer/create/<int:question_id>/',#답변등록
         views.answer_create, name='answer_create'),
    path('question/modify/<int:question_id>/', views.question_modify, #답변 수정
         name='question_modify'),
    path('question/delete/<int:question_id>/', #질문 삭제
         views.question_delete, name='question_delete'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, #답변삭제
         name='answer_delete'),
]