from unicodedata import name
from django.urls import path
from .views import *

urlpatterns=[
    path('signup/staff/', StaffSignUpView.as_view()),
    path('signup/student/', StudentSignUpView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='login'),
]

