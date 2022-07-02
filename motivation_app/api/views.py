from multiprocessing import context
from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken 

#views
class StaffSignUpView(generics.GenericAPIView):
    serializer_class=StaffSignUpSerializer
    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "Token":Token.objects.get(user=user).key,
            "message":"Registration successful"
        })

class StudentSignUpView(generics.GenericAPIView):
    serializer_class=StudentSignUpSerializer
    def post(self, request, *args, **kwargs):
        serializer= self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "Token":Token.objects.get(user=user).key,
            "message":"Registration successful"
        })
        
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user=serializer.validate_data['user']
        token, created=Token.objects.get_or_create(user=user)
        
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_staff':user.is_staff
        })