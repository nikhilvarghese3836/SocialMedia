from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

from django.shortcuts import render

from .models import User
from .serializers import UserSerializer,RegisterSerializer

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def get(self,request,*args,**kwargs):
    try:
      user = User.objects.get(id=request.user.id)
      serializer = UserSerializer(user)
      return Response(serializer.data)
    except Exception as e:
            return JsonResponse({'status':'failed','message':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

class UserFollowAPIView(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def post(self, request):
    try:
      user_id = request.data.get('id', None)
      if user_id:
          user_ins = User.objects.filter(id=user_id).first()
          if user_ins:
              user_ins.follows.add(request.user)
              return JsonResponse({"status":"success"}, status=HTTP_200_OK)
      return JsonResponse({}, status=HTTP_404_NOT_FOUND)
    except Exception as e:
            return JsonResponse({'status':'failed','message':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class UserUnfollowAPIView(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (IsAuthenticated,)
  def post(self, request):
    try:
      user_id = request.data.get('id', None)
      if user_id:
          user_ins = User.objects.filter(id=user_id).first()
          if user_ins:
              user_ins.follows.remove(request.user)
              return JsonResponse({"status":"success"}, status=HTTP_200_OK)
      return JsonResponse({}, status=HTTP_404_NOT_FOUND)
    except Exception as e:
            return JsonResponse({'status':'failed','message':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)