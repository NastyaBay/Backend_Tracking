from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Page, PageStatistics
from .serializer import PageSerializer, PageStatisticsSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class PageListView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user.id
        request_data = request.data.copy()
        request_data["user"] = user
        serializer = PageSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):

        user_pages = Page.objects.filter(user=request.user.id)
        serializer = PageSerializer(user_pages, many=True)
        return Response(serializer.data)

class PageDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, url):
        page = get_object_or_404(Page, page_link=url)
        if page.user != request.user:
            return Response({"detail": "Вы не имеете доступа к этой странице."}, status=status.HTTP_403_FORBIDDEN)
        serializer = PageSerializer(page)
        return Response(serializer.data)

    def put(self, request, url):
        page = get_object_or_404(Page, page_link=url)
        if page.user != request.user:
            return Response({"detail": "Вы не имеете доступа к этой странице."}, status=status.HTTP_403_FORBIDDEN)
        user = request.user.id
        request_data = request.data.copy()
        request_data["user"] = user
        serializer = PageSerializer(page, data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, url):
        page = get_object_or_404(Page, page_link=url)
        if page.user != request.user:
            return Response({"detail": "Вы не имеете доступа к этой странице."}, status=status.HTTP_403_FORBIDDEN)
        page.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PageStatisticsList(APIView):
    def get(self, request):
        statistics = PageStatistics.objects.all()
        serializer = PageStatisticsSerializer(statistics, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PageStatisticsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetSinglePageStatistic(APIView):
    def get(self, request, pk, format=None):
        try:
            pageStatistic = PageStatistics.objects.get(pk=pk)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PageStatisticsSerializer(pageStatistic)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            page_statistic = PageStatistics.objects.get(pk=pk)
        except PageStatistics.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PageStatisticsSerializer(page_statistic, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetDatePageStatistic(APIView):
    def get(self, request, date, format=None):
        try:
            page_statistic = PageStatistics.objects.get(date=date)
        except PageStatistics.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PageStatisticsSerializer(page_statistic)
        return Response(serializer.data)
