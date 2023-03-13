from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from . import serializers
from .models import User

class Users(APIView):

    # 유저 생성
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            serializer = serializers.UserSerializer(user)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
class LogIn(APIView):
    def get_user(self, username, password):
        try:
            user = User.objects.get(username=username, password=password)
            return user
        except User.DoesNotExist:
            raise NotFound
        
    
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            raise ParseError
        user = self.get_user(username, password)
        return Response({
                "detail": "로그인 성공",
                "username": user.username
        })
        
class LogOut(APIView):
    
    def post(self, request):
        return Response({"ok": "bye!"})