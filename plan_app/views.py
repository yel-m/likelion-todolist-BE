from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Plan
from . import serializers

from rest_framework.permissions import IsAuthenticated
class Plans(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        now = timezone.localtime(timezone.now()).month
        try:
            month = request.query_params.get("month", now)
            month = int(month)
        except ValueError:
            month = now
        all_plans = Plan.objects.filter(date__month=month)
        serializer = serializers.PlanSerializer(
            all_plans,
            many=True,
        )
        return Response(serializer.data)
        
        