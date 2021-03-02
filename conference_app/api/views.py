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

channel_layer = get_channel_layer()

def index(request):
    channel_name = request.GET['channel_name']
    print(channel_name)
    global a 
    # print(a.channels)
    # out = async_to_sync(a.group_send)('test_channel',{'type':'snd.msg','text':'HOW YOU DOING?'})
    async_to_sync(a.send)(channel_name,{'type':'snd.msg','text':'Hello'})
    out = async_to_sync(get_channel_layer().receive)('test_channel')
    print(out)
    # print('-'*20)
    return HttpResponse("Hello")


class JoinRoom(APIView):

    def get(self,request):
        room_id = request.GET['room_id']
        data = request.GET['data']
        print('Before:',channel_layer.channels)
        async_to_sync(channel_layer.group_send)(room_id,{'type':'send.offer','text':data})
        print("After:",channel_layer.channels)
        return HttpResponse(status.HTTP_200_OK)

    def post(self,request):
        room_id = 'abcd'
        print(channel_layer.channels)
        out = async_to_sync(channel_layer.receive)('offer')
        print(out)
        return HttpResponse(status.HTTP_200_OK)

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

