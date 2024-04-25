from django.urls import path
from .views import CreateForm, GetForms, GetSingleForm, QuestionForm, GetSingleQuestion, AnswerQuestion, GetSingleAnswer

urlpatterns = [
    path('forms/', GetForms.as_view(), name='get_forms'),
    path('forms/<int:pk>/', GetSingleForm.as_view(), name='get_single_form'),
    path('forms/create/', CreateForm.as_view(), name='create_form'),

    path('forms/<int:pk_form>/question/', QuestionForm.as_view(), name='question_page'),
    path('forms/question/<int:pk>/', GetSingleQuestion.as_view(), name='get_single_question'),

    path('question/<int:pk_question>/answer/', AnswerQuestion.as_view(), name='answer_question'),
    path('question/answer/<int:pk>/', GetSingleAnswer.as_view(), name='get_single_answer'),
]