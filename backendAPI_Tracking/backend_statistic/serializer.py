from rest_framework import serializers
from .models import UserStatistics

class StatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserStatistics
        fields = ['id', 'full_name', 'category', 'first_visit', 'last_visit', 'number_visits', 'number_forms']