from django.urls import path
from .views import CreatePage, GetPages, GetSinglePage, PageStatisticsList, GetSinglePageStatistic, GetDatePageStatistic

urlpatterns = [
    path('pages/', GetPages.as_view(), name='get_pages'),
    path('pages/<int:pk>/', GetSinglePage.as_view(), name='get_single_page'),
    path('pages/create/', CreatePage.as_view(), name='create_page'),
    path('pages/statistic/', PageStatisticsList.as_view(), name='statistic_page'),
    path('pages/statistic/<int:pk>/', GetSinglePageStatistic.as_view(), name='get_single_statistic_page'),
    path('pages/statistic/date/<str:date>/', GetDatePageStatistic.as_view(), name='get_date_statistic_page'),
]