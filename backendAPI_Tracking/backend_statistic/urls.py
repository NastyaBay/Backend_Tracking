from django.urls import path
from .views import Statistic, GetSingleStatistic

urlpatterns = [
    path('statistic/', Statistic.as_view(), name='get_post_statistic'),
    path('statistic/<int:pk>/', GetSingleStatistic.as_view(), name='get_put_single_statistic'),
]