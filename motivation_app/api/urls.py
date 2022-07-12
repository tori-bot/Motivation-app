from unicodedata import name
from django.urls import path
from .views import *

urlpatterns=[
    # path('signup/admin/', AdminSignUpView.as_view()),
    # path('signup/staff/', StaffSignUpView.as_view()),
    # path('signup/student/', StudentSignUpView.as_view()),
    # path('login/', CustomAuthToken.as_view(), name='login'),
    path('user/', GetUser.as_view()),
    path('signup/', UserSignUp.as_view(), name='signup'),
    path('login/', UserLogin.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('staff/dashboard/', StaffOnlyView.as_view(), name='staff'),
    path('student/dashboard/', StudentOnlyView.as_view(), name='student')
]

