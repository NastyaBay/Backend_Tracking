from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Page, PageStatistics
from .serializer import PageSerializer, PageStatisticsSerializer

# Create your views here.
class CreatePage(APIView):
    def post(self, request, format=None):
        serializer = PageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetPages(APIView):
    def get(self, request, format=None):
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response(serializer.data)

class GetSinglePage(APIView):
    def get(self, request, pk, format=None):
        try:
            page = Page.objects.get(pk=pk)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = PageSerializer(page)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            page = Page.objects.get(pk=pk)
        except Page.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PageSerializer(page, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
