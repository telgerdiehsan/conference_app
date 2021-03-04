from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404,HttpResponse ,JsonResponse
from google.oauth2 import id_token
from google.auth.transport import requests
from api.models import User,Rooms
from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
import random
import string

def get_random_string(length):

    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


class Room(APIView):

    def get(self,request):
        return JsonResponse(Rooms.objects.all())

    def post(self,request):
        room_id = get_random_string(8)
        room = Rooms(room_id=room_id)
        try:
            room.save()
            return JsonResponse({'room_id':room_id})
        except Exception as e:
            print(e)
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)
    
class googleLogin(APIView):

    # def get(self,request):
    #     return HttpResponse(status=status.HTTP_200_OK)
    def get(self,request):
        return HttpResponse(status=status.HTTP_200_OK)
    def post(self,request):
        token = request.data['google']
        try:
            idinfo = id_token.verify_oauth2_token(token['uc']['id_token'], requests.Request())
            
            return HttpResponse(status=status.HTTP_200_OK)
        except Exception as e:
            return HttpResponse(status=status.HTTP_403_FORBIDDEN)

