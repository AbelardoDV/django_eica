from rest_framework import serializers
from api.models import DRFPost


class DRFPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPost
        fields = '__all__'
