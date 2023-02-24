from rest_framework import serializers
from .models import Plan

class PlanSerializer(serializers.ModelSerializer):
    
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Plan
        fields = "__all__"
        