from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import generics
from django.http import JsonResponse
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_500_INTERNAL_SERVER_ERROR
)

from usermodel.models import User
from .models import Posts
import os
from django.conf import settings
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
import json
from django.core.cache import cache


class AddPostAPIView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            text = request.data.get('text', None)
            ins_post = Posts.objects.create(
                post_by = request.user,
                text=text,
            )
            str_file = ''
            base_dir = os.path.dirname(os.path.dirname(__file__))
            for file in request.FILES.getlist('media'):
                file_name = settings.MEDIA_ROOT + '-'.join(file.name.split(' '))
                path = default_storage.save(file_name, ContentFile(file.read()))
                str_file += settings.MEDIA_URL + '-'.join(file.name.split(' ')) + ','
            ins_post.media_url = str_file
            ins_post.save()
            follow_list = request.user.follows.values_list('id',flat=True)
            for key in follow_list:
                if cache.has_key(key):
                    data = json.loads(cache.get(key))
                    data.append(ins_post.serialize())
                    cache.set(key, json.dumps(data))
                else:
                    cache.set(key, json.dumps([ins_post.serialize()]))

            return JsonResponse({"status":"success", "data":ins_post.serialize()}, status=HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'status':'failed','message':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request):
        try:
            id = request.data.get('id')
            if id:
                ins_post = Posts.objects.filter(id=id, post_by=request.user)
                if ins_post:
                    follow_list = request.user.follows.values_list('id',flat=True)
                for key in follow_list:
                    if cache.has_key(key):
                        data = json.loads(cache.get(key))
                        data.remove(ins_post[0].serialize())
                        cache.set(key, json.dumps(data))
                ins_post.delete()
                return JsonResponse({"status":"success"}, status=HTTP_200_OK)
            return JsonResponse({}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            return JsonResponse({'status':'failed','message':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)

class GetPostFeedAPIView(APIView):
    authentication_classes = (TokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        try:
            key = request.user.id
            data = []
            if cache.has_key(key):
                data = json.loads(cache.get(key))
            return JsonResponse({"status":"success", "data":data}, status=HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'status':'failed','message':str(e)}, status=HTTP_500_INTERNAL_SERVER_ERROR)