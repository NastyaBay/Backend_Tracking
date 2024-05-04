from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404

from .models import Form, Question, Answer
from .serializer import FormViewSerializer
from .serializer import FormSerializerRead, FormSerializerWrite

# Create your views here.

class FormListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        forms = Form.objects.filter(user=request.user.id)
        serializer = FormViewSerializer(forms, many=True)
        return Response(serializer.data)

    def post(self, request):
        user = request.user.id
        request_data = request.data.copy()
        request_data['user'] = user
        serializer = FormViewSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, url):
        form = get_object_or_404(Form, form_link=url)
        serializer = FormSerializerRead(form)
        return Response(serializer.data)

    def put(self, request, url):
        form = get_object_or_404(Form, form_link=url)
        serializer = FormSerializerWrite(instance=form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, url):
        form = get_object_or_404(Form, form_link=url)
        form.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)