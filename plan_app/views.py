from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
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
        all_plans = Plan.objects.filter(date__month=month, user=request.user)
        serializer = serializers.PlanSerializer(
            all_plans,
            many=True,
        )
        return Response(serializer.data)
        
    def post(self, request):
        
        serializer = serializers.PlanSerializer(data=request.data)
        if serializer.is_valid():
            plan = serializer.save(
                user=request.user
            )
            return Response(serializers.PlanSerializer(plan).data)
        else:
            return Response(serializer.errors)

class PlanDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, id, user):
        try:
            return Plan.objects.get(id=id, user=user)
        except Plan.DoesNotExist:
            raise NotFound
    
    def put(self, request, id):
        plan = self.get_object(id, request.user)
        
        serializer = serializers.PlanSerializer(
            plan,
            data=request.data,
            partial=True,
        )
        
        if serializer.is_valid():
            updated_plan = serializer.save()
            return Response(serializers.PlanSerializer(updated_plan).data)
        else:
            return Response(serializer.errors)
        
    def delete(self, request, id):
        plan = self.get_object(id, request.user)
        plan.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    

class PlanCheck(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, id):
        try:
            return Plan.objects.get(id=id)
        except Plan.DoesNotExist:
            raise NotFound
    
    def put(self, request, id):
        plan = self.get_object(id, request.user)
        serializer = serializers.PlanSerializer(
            plan,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            updated_plan = serializer.save()
            return Response(serializers.PlanSerializer(updated_plan).data)
        else:
            return Response(serializer.errors)

class PlanReview(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, id):
        try:
            return Plan.objects.get(id=id)
        except Plan.DoesNotExist:
            raise NotFound
    
    def put(self, request, id):
        plan = self.get_object(id, request.user)
        serializer = serializers.PlanSerializer(
            plan,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            updated_plan = serializer.save()
            return Response(serializers.PlanSerializer(updated_plan).data)
        else:
            return Response(serializer.errors)