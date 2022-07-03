from django.urls import path
from . import views
from .api.views import *

urlpatterns = [
    path('', views.home,name='home'),
    path('signup/staff/', StaffSignUpView.as_view()),
    path('signup/student/', StudentSignUpView.as_view()),
    path('staff/create_categories/',views.categoryCreation, name="category"),
    path('staff/post/', views.PostList.as_view(), name='staffpostendpoint'),
    path('staff/post/<int:pk>/', views.SinglePostList.as_view(), name='singlepost'),
]
