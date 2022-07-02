from rest_framework import generics
from rest_framework.response import Response
from .serializers import *
from rest_framework.authtoken.models import Token

#views
class StaffSignUpView(generics.GenericAPIView):
    serializer_class=StaffSignUpSerializer
    
    def post(self, request, *args, **kwargs):
        serializer= serializer.get_serializer(data=request.data)
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
        serializer= serializer.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user":UserSerializer(user, context=self.get_serializer_context()).data,
            "Token":Token.objects.get(user=user).key,
            "message":"Registration successful"
        })