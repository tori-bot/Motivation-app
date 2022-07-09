from cgitb import lookup
from django.db import IntegrityError
from django.http import Http404
from django.shortcuts import render
from .api.serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Wishlist as WishlistModel
# Application views.


class profile(APIView):
    def get(request, format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles, many=True)
        return Response(serializers.data)


class UpdateProfile(APIView):
    serializer_class = ProfileSerializer
    lookup_field = 'email'
    profiles = Profile.objects.all()

    def put(self, request, *args, **kwargs):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['POST'])
class categoryCreation(APIView):
    def get(self, request, format=None):
        # querying from the database(Posts table)
        categories = Category.objects.all()
        serializers = CategorySerializer(categories, many=True)
        # JSON RESPONSE
        return Response(serializers.data)
    
    
    def post(request):
        user = request.user
        user = Category(user=user)

        serializer = CategorySerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["success"] = "Post category created successfully!"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostList(APIView):
    def get(self, request, format=None):
        # querying from the database(Posts table)
        posts = Post.objects.all()
        serializers = PostSerializer(posts, many=True)
        # JSON RESPONSE
        return Response(serializers.data)

    # permission_classes = (IsAdminOrReadOnly,)

    def post(self, request, format=None):
        serializers = PostSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SinglePostList(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get_single_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        single_post = self.get_single_post(pk)
        serializers = PostSerializer(single_post)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        single_post = self.get_single_post(pk)
        serializers = PostSerializer(single_post, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        flag_post = self.get_single_post(pk)
        flag_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['POST'])


class PostComment(APIView):
    def get_single_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        single_post = self.get_single_post(pk)
        serializers = PostSerializer(single_post)
        return Response(serializers.data)

        
    def post(self, request, pk, format=None):
        serializers = CommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PostChildComment(APIView):  
    def get_single_comment(self, pk):
            try:
                return Comment.objects.get(pk=pk)
            except Comment.DoesNotExist:
                return Http404

    def get(self, request, pk, format=None):
        single_comment= self.get_single_comment(pk)
        serializers = CommentSerializer(single_comment)
        return Response(serializers.data)

        
    def post(self, request, pk, format=None):
        serializers = ChildCommentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
class commentsList(APIView):
    def get(self, request, format=None):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
class LikesList(APIView):
    def get(self, request, format=None):
        likes = Likes.objects.all()
        serializer = CommentSerializer(likes, many=True)
        return Response(serializer.data)

class StudentList(APIView):
    def get_student(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Http404

    def get(self, request, format=None):
        #querying from the database(Student table)
        students = Student.objects.all()
        serializers = StudentSerializer(students, many=True)
        #JSON RESPONSE
        return Response(serializers.data)
    
    
    # permission_classes = (IsAdminOrReadOnly,)
    
    def post(self, request, format=None):
        serializers = StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    

class SingleStudent(APIView):
    # permission_classes = (IsAdminOrReadOnly,)
    def get_student(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        single_post = self.get_student(pk)
        serializers = StudentSerializer(single_post)
        return Response(serializers.data)
    
    
    def put(self, request, pk, format=None):
        single_post = self.get_student(pk)
        serializers = StudentSerializer(single_post, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        flag_post = self.get_student(pk)
        flag_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, pk,format=None):
        serializers=StudentSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class LikesView(APIView):
    def post(self, request, pk):
        user=request.user
        # current_user = request.user
        user_id = User.objects.get(id=user.id)
        # user_id=User.objects.get(id=user.id)
        # user_id = User.objects.get(id=user)
        try:
            post_id = Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            post_id = None
      # get_object_or_404(Likes, pk=post_id)
        check = Likes.objects.filter(Q(user_id=user_id) & Q(post_id=post_id))
       # check=Likes.object.get_object_or_404(Likes, pk=post_id)
        if(check.exists()):
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "You only like once"
            })
        new_like = Likes.objects.create(user_id=user_id, post_id=post_id)
        new_like.save()
        serializer = LikesSerializer(new_like)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RegisteredUsers(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    

class DeactivateUser(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user=self.request.user
        user.delete()

        return Response({"result":"user delete"})

 
# Admin

class Wishlist(APIView):

    def get_student(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Http404

    def get_single_post(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            return Http404


    def get(self, request,pk, format=None):
        items=WishlistModel.objects.filter(student_id=pk)
        serializers = WishlistSerializer(items,many=True)
        return Response(serializers.data)

    def post(self, request,pk,format=None):
        
        serializers=WishlistSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleWishlist(APIView):
    def get_single_wishlist(self, pk):
        try:
            return WishlistModel.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        user = self.get_single_wishlist(pk)
        serializers = WishlistSerializer(user)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        single_post = self.get_single_wishlist(pk)
        serializers = WishlistSerializer(single_post, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        flag_post = self.get_single_wishlist(pk)
        flag_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def post(self, request, pk,format=None):
        serializers=WishlistSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class AddUser(APIView):
    pass

class Subscriptions(APIView):
    def get_single_sub(self, pk):
        try:
            return Subscription.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return Http404

    def get(self, request,pk, format=None):
            items=Subscription.objects.filter(student_id=pk)
            serializers = SubscriptionSerializer(items,many=True)
            return Response(serializers.data)

    def post(self, request,pk,format=None):
        serializers=SubscriptionSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        single_post = self.get_single_sub(pk)
        serializers = SubscriptionSerializer(single_post, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, format=None):
        flag_post = self.get_single_sub(pk)
        flag_post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
