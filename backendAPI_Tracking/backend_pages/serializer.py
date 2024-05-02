from rest_framework import serializers
from .models import Page, PageStatistics

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'user', 'published', 'title', 'page_link', 'qr_link', 'json_data']

class PageStatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PageStatistics
        fields = ['id', 'page', 'date', 'views', 'visits', 'unique_users', 'visits_phone',  'visits_comp', 'click_links']