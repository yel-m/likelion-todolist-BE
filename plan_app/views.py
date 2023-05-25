from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Plan, User
from . import serializers


class Plans(APIView):
    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise NotFound
            
    
    def get(self, request, username):
        now = timezone.localtime(timezone.now()).month
        try:
            month = request.query_params.get("month", now)
            month = int(month)
        except ValueError:
            month = now
        user = self.get_user(username)
        all_plans = Plan.objects.filter(date__month=month, user=user)
        serializer = serializers.PlanSerializer(
            all_plans,
            many=True,
        )
        return Response(serializer.data)
        
    def post(self, request, username):
        
        serializer = serializers.PlanSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_user(username)
            plan = serializer.save(
                user=user
            )
            return Response(serializers.PlanSerializer(plan).data)
        else:
            return Response(serializer.errors)

class PlanDetail(APIView):
    
    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise NotFound
    
    def get_object(self, id, user):
        try:
            return Plan.objects.get(id=id, user=user)
        except Plan.DoesNotExist:
            raise NotFound
    
    def patch(self, request, username, id):
        user = self.get_user(username)
        plan = self.get_object(id, user)
        
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
        
    def delete(self, request, username, id):
        plan = self.get_object(id, self.get_user(username))
        plan.delete()
        return Response(status=HTTP_204_NO_CONTENT)
    

class PlanCheck(APIView):
    
    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise NotFound
    
    def get_object(self, id, user):
        try:
            return Plan.objects.get(id=id, user=user)
        except Plan.DoesNotExist:
            raise NotFound
    
    def patch(self, request, username, id):
        user = self.get_user(username)
        plan = self.get_object(id, user)
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
    
    def get_user(self, username):
        try:
            user = User.objects.get(username=username)
            return user
        except User.DoesNotExist:
            raise NotFound
    
    def get_object(self, id, user):
        try:
            return Plan.objects.get(id=id, user=user)
        except Plan.DoesNotExist:
            raise NotFound
    
    def patch(self, request, username, id):
        user = self.get_user(username)
        plan = self.get_object(id, user)
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