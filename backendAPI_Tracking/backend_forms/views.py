from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Form, Question, Answer
from .serializer import FormSerializer, QuestionSerializer, AnswerSerializer

# Create your views here.
class CreateForm(APIView):
    def post(self, request, format=None):
        serializer = FormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetForms(APIView):
    def get(self, request, format=None):
        forms = Form.objects.all()
        serializer = FormSerializer(forms, many=True)
        return Response(serializer.data)

class GetSingleForm(APIView):
    def get(self, request, pk, format=None):
        try:
            form = Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = FormSerializer(form)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            form = Form.objects.get(pk=pk)
        except Form.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = FormSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuestionForm(APIView):
    def post(self, request, pk_form, format=None):
        data = request.data.copy()
        data['form'] = pk_form
        serializer = QuestionSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk_form, format=None):
        questions = Question.objects.filter(form=pk_form)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

class GetSingleQuestion(APIView):
    def get(self, request, pk, format=None):
        try:
            question = Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)



class AnswerQuestion(APIView):
    def post(self, request, pk_question, format=None):
        data = request.data.copy()
        data['question'] = pk_question
        serializer =AnswerSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk_question, format=None):
        answer = Answer.objects.filter(question=pk_question)
        serializer = AnswerSerializer(answer, many=True)
        return Response(serializer.data)


class GetSingleAnswer(APIView):
    def get(self, request, pk, format=None):
        try:
            answer = Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer =AnswerSerializer(answer)
        return Response(serializer.data)