from rest_framework import serializers
from motivation_app.models import *
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        
# class AdminSignUpSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
#     class Meta:
#         model=User
#         fields=['username', 'email','password', 'password2']
        
#         extra_kwargs={
#             'password':{'write_only':'True'}
#         }
        
        
#     def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],   
#         )
#         password=self.validated_data['password']
#         password2=self.validated_data['password']
        
#         if password != password2:
#             raise serializers.ValidationError({'error':'check your passwords'})
#         user.set_password(password)
#         user.is_admin=True
#         user.save()
#         Admin.objects.create(user=user)
#         return user
        

# class StaffSignUpSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
#     class Meta:
#         model=User
#         fields=['username', 'email','password', 'password2']
        
#         extra_kwargs={
#             'password':{'write_only':'True'}
#         }
        
        
#     def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],   
#         )
#         password=self.validated_data['password']
#         password2=self.validated_data['password']
        
#         if password != password2:
#             raise serializers.ValidationError({'error':'check your passwords'})
#         user.set_password(password)
#         user.is_staff=True
#         user.save()
#         Staff.objects.create(user=user)
#         return user
            
# class StudentSignUpSerializer(serializers.ModelSerializer):
#     password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
#     class Meta:
#         model=User
#         fields=['username', 'email','password', 'password2']
        
#         extra_kwargs={
#             'password':{'write_only':'True'}
#         }
        
        
#     def save(self, **kwargs):
#         user=User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],   
#         )
#         password=self.validated_data['password']
#         password2=self.validated_data['password']
        
#         if password != password2:
#             raise serializers.ValidationError({'error':'check your passwords'})
#         user.set_password(password)
#         user.is_student=True
#         user.save()
#         Student.objects.create(user=user)
#         return user
            
            
class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
        read_only_fields = ["name"]
        
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True)

    def validate_user(self):
        user = authenticate(
            username=self.validated_data["username"],
            password=self.validated_data["password"],
        )
        if user is None:
            raise serializers.ValidationError("Invalid Credentials")
        return user
        
#User profile serializers
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("pk", 'user','firstname','lastname','email','profile_pic','bio') 
        
        
class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name","password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
   
        
        

class CategorySerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model=Category
        fields = '__all__'
        
class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # content_image = serializers.ImageField(required=False)

    class Meta:
        model=Post
        fields = '__all__'
       
     
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model=Comment
        fields = '__all__'
        # fields = (
        #     'id',
        #      user''
        #     'comment',
        #     'date_posted',
        #     'user_id',
        #     'post_id'
        # )
        
class ChildCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model=ChildComment
        fields = '__all__'
    
class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Likes
        fields = '__all__'

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class UserProfileChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class GetUserSerializer(serializers.ModelSerializer):
    # role = RoleSerializer(read_only=True)
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name", "role"]