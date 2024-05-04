from rest_framework import serializers
from .models import Form, Question, Answer

class AnswerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['id', 'title_answer']

class QuestionsSerializerRead(serializers.ModelSerializer):
    answers = AnswerDetailSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title_question', 'type', 'answers']

class QuestionsSerializerWrite(serializers.ModelSerializer):
    answers = AnswerDetailSerializer(many=True)

    class Meta:
        model = Question
        fields = ['id', 'title_question', 'type', 'answers']

class FormViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = '__all__'

class FormSerializerRead(serializers.ModelSerializer):
    questions = QuestionsSerializerRead(many=True, read_only=True)

    class Meta:
        model = Form
        fields = ['id', 'title', 'form_link', 'json_data', 'questions']

class FormSerializerWrite(serializers.ModelSerializer):
    questions = QuestionsSerializerWrite(many=True)

    class Meta:
        model = Form
        fields = ['id', 'title', 'form_link', 'json_data', 'questions']

    def update(self, instance, validated_data):
        instance.json_data = validated_data.get('json_data', instance.json_data)
        instance.title = validated_data.get('title', instance.title)

        instance.questions.all().delete()

        questions_data = validated_data.pop('questions', [])
        for question_data in questions_data:
            answers_data = question_data.pop('answers', [])
            question = Question.objects.create(form=instance, **question_data)
            for answer_data in answers_data:
                Answer.objects.create(question=question, **answer_data)

        instance.save()
        return instance