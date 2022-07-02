from django.shortcuts import render
from .api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.
def home(request):
    return render(request, 'index.html')

@api_view(['POST'])
def categoryCreation(request):
    user = request.user
    user = Category(user = user)
    
    serializer = CategorySerializer(user, data=request.data)
    data={}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "Post category created successfully!"
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PostList(APIView):
    def get(self, request, format=None):
        #querying from the database(students table)
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True)
        
        #JSON RESPONSE
        return Response(serializers.data)
    
    
    # permission_classes = (IsAdminOrReadOnly,)
    
    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)