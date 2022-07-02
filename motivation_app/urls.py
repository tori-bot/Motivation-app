from django.urls import path
from . import views
from .api.views import *

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/staff/', StaffSignUpView.as_view()),
    path('signup/student/', StudentSignUpView.as_view()),
]