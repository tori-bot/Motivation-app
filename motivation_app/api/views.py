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
from rest_framework.parsers import FileUploadParser
from django.contrib.auth import authenticate, login, logout

#views
# class AdminSignUpView(generics.GenericAPIView):
#     serializer_class=AdminSignUpSerializer
#     def post(self, request, *args, **kwargs):
#         serializer= self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user=serializer.save()
#         return Response({
#             "user":UserSerializer(user, context=self.get_serializer_context()).data,
#             "Token":Token.objects.get(user=user).key,
#             "message":"Admin Registration successful.You are now registered as an admin"
#         })

# class StaffSignUpView(generics.GenericAPIView):
#     serializer_class=StaffSignUpSerializer
#     def post(self, request, *args, **kwargs):
#         serializer= self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user=serializer.save()
#         return Response({
#             "user":UserSerializer(user, context=self.get_serializer_context()).data,
#             "Token":Token.objects.get(user=user).key,
#             "message":"Staff Registration successful.You are now registered as a staff"
#         })

# class StudentSignUpView(generics.GenericAPIView):
#     serializer_class=StudentSignUpSerializer
#     def post(self, request, *args, **kwargs):
#         serializer= self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         user=serializer.save()
#         return Response({
#             "user":UserSerializer(user, context=self.get_serializer_context()).data,
#             "Token":Token.objects.get(user=user).key,
#             "message":"Student Registration successful.You are now registered as a student"
#         })
        
        
class UserLogin(APIView):
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self, request, format=None):
        data = {}
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validate_user()
            data = { "message": "User logged in successfully",
                     "username":user.username,
                      "role": user.role,
                      
                      }

            # get user token
            token, created = Token.objects.get_or_create(user=user)
            data["token"] = token.key
            
            responseStatus = status.HTTP_200_OK
            return Response(data, status=responseStatus)

        else:
            data = serializer.errors
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


class UserSignUp(APIView):
    @swagger_auto_schema(request_body=SignUpSerializer)
    def post(self, request, format=None):
        data=request.data
        print (data)
        email=data['email']
        if '@admin' in email:
            role = 1
        elif '@staff' in email:
            role = 2
        elif '@student' in email:
            role = 3
        else:
            return Response( status=status.HTTP_400_BAD_REQUEST)

                 
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(role=role)
            # return success message
            data = {"username":data['username'],
                      "email":data['email'],
                      "message": "User created successfully",
                      }
                   
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class CustomAuthToken(ObtainAuthToken):
#     def post(self, request, *args, **kwargs):
#         serializer=self.serializer_class(data=request.data, context={'request':request})
#         serializer.is_valid(raise_exception=True)
#         user=serializer.validated_data['user']
#         token, created=Token.objects.get_or_create(user=user)
        
#         return Response({
#             'token':token.key,
#             'user_id':user.pk,
#             'is_staff':user.is_staff
#         })
        
class LogoutView(APIView):
    def get(self,request, format=None):
        # request.auth.delete()
        logout(request)
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
    
    
class GetUser(APIView):
    def post(self, request, format=None):
        token = request.data.get("token")
        if token is None:
            data = {"token": "Missing Token"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
        try:
            user = Token.objects.get(key=token).user
            serializer = GetUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        # checks if token is invalid
        except Token.DoesNotExist:
            data = {"token": "Invalid Token"}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)
