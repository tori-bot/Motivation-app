from dataclasses import fields
from django.forms import CharField
from rest_framework import serializers
from motivation_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'password']
        
class StaffSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    
    class Meta:
        model=User
        fields=['username', 'email','password', 'password2']
        
        extra_kwargs={
            'password':{'write_only':'True'}
        }
        
        
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],   
        )
        password=self.validated_data['password']
        password2=self.validated_data['password']
        
        if password != password2:
            raise serializers.ValidationError({'error':'check your passwords'})
        user.set_password(password)
        user.is_staff=True
        user.save()
        Staff.objects.create(user=user)
        return user
            
class StudentSignUpSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields=['username', 'email','password', 'password2']
        
        extra_kwargs={
            'password':{'write_only':'True'}
        }
        def save(self,*args, **kwargs):
            user=User(
                username=self.validated_data['username'],
                email=self.validated_data['email'],    
            )
            password=self.validated_data['password']
            password2=self.validated_data['password']
            
            if password != password2:
                raise serializers.ValidationError({'error':'check your passwords'})
            user.set_password(password)
            user.is_student=True
            user.save()
            Student.objects.create(user=user)
            return user
        
        
#User profile serializers
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ("pk", 'user','firstname','lastname','email','profile_pic','bio') 
        
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields = '__all__'
        