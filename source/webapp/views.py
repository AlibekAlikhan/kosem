from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import GenericAPIView
from accounts.serializers import UserSerializer, LoginSerializer


class NewAcsesView(GenericAPIView):


    def get(self, request):
        return render(request, 'new_acses.html')