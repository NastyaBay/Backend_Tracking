from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserStatistics
from .serializer import StatisticSerializer

# Create your views here.
class Statistic(APIView):
    def post(self, request, format=None):
        serializer = StatisticSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        userStatistics = UserStatistics.objects.all()
        serializer = StatisticSerializer(userStatistics, many=True)
        return Response(serializer.data)

class GetSingleStatistic(APIView):
    def get(self, request, pk, format=None):
        try:
            userStatistics = UserStatistics.objects.get(pk=pk)
        except UserStatistics.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = StatisticSerializer(userStatistics)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            form = UserStatistics.objects.get(pk=pk)
        except UserStatistics.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = StatisticSerializer(form, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)