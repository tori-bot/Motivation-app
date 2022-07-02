from multiprocessing import context
from rest_framework import generics
from rest_framework.response import Response

from motivation_app.api.permissions import IsStaffUser,IsStudentUser
from .serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken 
from rest_framework.views import APIView
from rest_framework import status, permissions
from drf_yasg.utils import swagger_auto_schema
from rest_framework.schemas import get_schema_view

#views
# @swagger_auto_schema(request_body=StaffSignUpSerializer)
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
        user=serializer.validated_data['user']
        token, created=Token.objects.get_or_create(user=user)
        
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_staff':user.is_staff
        })
        
class LogoutView(APIView):
    def post(self,request, format=None):
        request.auth.delete()
        return Response(status=status.HTTP_200_OK)
    
class StaffOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsStaffUser]
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user
    
class StudentOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsStudentUser]
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user