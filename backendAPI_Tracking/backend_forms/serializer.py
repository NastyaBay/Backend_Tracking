from rest_framework import serializers
from .models import Form, Question, Answer

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = ['id', 'user', 'title', 'form_link', 'qr_link']

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'form', 'title_question']

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'question', 'title_answer', 'sum_answer']