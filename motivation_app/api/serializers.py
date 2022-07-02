from dataclasses import fields
from django.forms import CharField
from rest_framework import serializers
from motivation_app.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_student']
        
class StaffSignUpSerializer(serializers.ModelSerializer):
    password2=CharField(style={'input_type':'password'})
    
    class Meta:
        model=User
        fields=['username', 'email', 'password2']
        
        extra_kwargs={
            'password':{'write_only':'True'}
        }
        
        
def save(self, **kwargs):
    user=User(
        username=self.validated_data['username'],
        email=self.validated_data['email'],
        
    )
    password=self.validated_data['password'],
    password2=self.validated_data['password'],
    
    if password != password2:
        raise serializers.ValidationError({'error':'check your passwords'})
    user.set_password(password)
    user.is_staff=True
    user.save()
    Staff.objects.create(user=user)
    return user
        
class StudentSignUpSerializer(serializers.ModelSerializer):
    password2=CharField(style={'input_type':'password'})
    
    class Meta:
        model=User
        fields=['username', 'email', 'password2']
        
        extra_kwargs={
            'password':{'write_only':'True'}
        }