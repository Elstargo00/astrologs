from rest_framework import serializers
from zodioscope.models import ZodioscopeDaily


class ZodioscopeDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = ZodioscopeDaily
        fields = (
            'id', 'date_range', 'sign', 'current_date', 
            'description', 'compatibility', 'mood',
            'color', 'lucky_number', 'lucky_time',
        )

