from rest_framework import generics
from rest_framework.response import Response
from .serializers import *

class StudentSignUpView(generics.GenericAPIView):
    serializer_class=StaffSignUpSerializer
    
    def post