from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404,HttpResponse 
from google.oauth2 import id_token
from google.auth.transport import requests
from api.models import User
# from google.oauth2
# Create your views here.


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

