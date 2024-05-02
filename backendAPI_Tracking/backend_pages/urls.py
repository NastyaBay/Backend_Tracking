from django.urls import path
from .views import PageListView, PageDetailView, PageStatisticsList, GetSinglePageStatistic, GetDatePageStatistic

urlpatterns = [
    path('pages/', PageListView.as_view(), name='pages_list'),
    path('pages/<str:url>/', PageDetailView.as_view(), name='get_single_page'),
    path('pages/statistic/', PageStatisticsList.as_view(), name='statistic_page'),
    path('pages/statistic/<int:pk>/', GetSinglePageStatistic.as_view(), name='get_single_statistic_page'),
    path('pages/statistic/date/<str:date>/', GetDatePageStatistic.as_view(), name='get_date_statistic_page'),
]