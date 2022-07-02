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
        
class StudentSignUpSerializer(serializers.ModelSerializer):
    password2=CharField(style={'input_type':'password'})
    
    class Meta:
        model=User
        fields=['username', 'email', 'password2']
        
        extra_kwargs={
            'password':{'write_only':'True'}
        }