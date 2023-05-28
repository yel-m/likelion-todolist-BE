from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_204_NO_CONTENT
from .models import Plan, User
from . import serializers


class Plans(APIView):
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
    
    def get(self, request, user_id):
        now = timezone.localtime(timezone.now())
        current_month = now.month
        current_day = now.day
        try:
            month = request.query_params.get("month", current_month)
            month = int(month)
        except ValueError:
            month = current_month
        try:
            day = request.query_params.get("day", current_day)
            day = int(day)
        except ValueError:
            day = current_day
        user = self.get_user(user_id)
        all_plans = Plan.objects.filter(
            date__month=month,
            date__day=day,
            user=user
        )
        serializer = serializers.PlanSerializer(
            all_plans,
            many=True,
        )
        return Response(serializer.data)
        
    def post(self, request, user_id):
        serializer = serializers.PlanSerializer(data=request.data)
        if serializer.is_valid():
            user = self.get_user(user_id)
            plan = serializer.save(
                user=user
            )
            return Response(serializers.PlanSerializer(plan).data)
        else:
            return Response(serializer.errors)

class PlanDetail(APIView):
    
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
    
    def get_plan(self, id, user):
        try:
            return Plan.objects.get(id=id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
    
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        
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
        
    def delete(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
        plan.delete()
        return Response(
            {
                "message": "삭제 성공"
            },
            status=HTTP_204_NO_CONTENT
        )

class PlanCheck(APIView):
    
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
    
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
    
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
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
    
    def get_user(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise NotFound("유저를 찾을 수 없습니다.")
    
    def get_plan(self, plan_id, user):
        try:
            return Plan.objects.get(id=plan_id, user=user)
        except Plan.DoesNotExist:
            raise NotFound("일정을 찾을 수 없습니다.")
    
    def patch(self, request, user_id, plan_id):
        user = self.get_user(user_id)
        plan = self.get_plan(plan_id, user)
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