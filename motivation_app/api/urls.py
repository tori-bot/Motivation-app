from unicodedata import name
from django.urls import path
from .views import *

urlpatterns=[
    path('signup/staff/', StaffSignUpView.as_view()),
    path('signup/student/', StudentSignUpView.as_view()),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('staff/dashboard/', StaffOnlyView.as_view(), name='staff'),
    path('student/dashboard/', StudentOnlyView.as_view(), name='student')
]

