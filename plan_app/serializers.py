from rest_framework import serializers
from .models import Plan

class PlanListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Plan
        fields = "__all__"
        