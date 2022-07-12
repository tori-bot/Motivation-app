from django.urls import path
from . import views
from .api.views import *
from rest_framework.schemas import get_schema_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Software Development Students motivation app",
        default_version='v1',
        description="Software Development Students motivation app REST API",
        terms_of_service="https://www.sds.com/policies/terms/",
        contact=openapi.Contact(email="contact@sds.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    #staff Urls
    
    
    # path('signup/staff/', StaffSignUpView.as_view()),
    # path('signup/student/', StudentSignUpView.as_view()),
    path('signup/',UserSignUp.as_view()),
    path('api/profile/', views.profile.as_view(),name='profile'),
    path('api/update_profile/', views.UpdateProfile.as_view(), name='profile_update'),
    path('staff/create_categories/',views.categoryCreation.as_view(), name="category"),
    path('staff/post/', views.PostList.as_view(), name='staffpostendpoint'),
    path('staff/post/<int:pk>', views.SinglePostList.as_view(), name='singlepost'),
    path('comment-staff/post/<int:pk>', views.PostComment.as_view(), name='comment'),
    path('staff/post/comment/<int:pk>/comment/', views.PostChildComment.as_view(), name='comment'),
    path('posts/<int:pk>/like/',views.LikesView.as_view(),name = 'post_likes'),
    
    
    #student urls
    path('student/update_profile/', views.UpdateProfile.as_view(), name='student_profile_update'),
    path('student/', views.StudentList.as_view(), name='studentslistendpoint'),
    path('student/<int:pk>/', views.SingleStudent.as_view(), name='singlestudent'),
    path('student/post/', views.PostList.as_view(), name='studentpostendpoint'),
    path('student/post/<int:pk>/', views.SinglePostList.as_view(), name='singlepost'),
    path('student/<int:pk>/wishlist/', views.Wishlist.as_view(), name='studentwishlistendpoint'),
    path('student/wishlist/<int:pk>/', views.SingleWishlist.as_view(), name='studentwishlistendpoint'),
    path('student/post/<int:pk>/like/',views.LikesView.as_view(),name = 'post_likes'),
    path('student/post/<int:pk>/comment/', views.PostComment.as_view(), name='comment'),
    
    
    
    #Admin Urls
    path('main/post/<int:pk>/', views.SinglePostList.as_view(), name='singlepost'),
    path('main/add_users/', views.AddUser.as_view(), name='users'),
    path('main/deactivate/', views.DeactivateUser.as_view(), name='deactivate'),
    
    #General apiendpoints
    path('all_users/', views.RegisteredUsers.as_view(), name='all_users'),
    path('all_comments/', views.commentsList.as_view(), name='comments'),
    path('all_likes/', views.LikesList.as_view(), name='likes'), 
]
