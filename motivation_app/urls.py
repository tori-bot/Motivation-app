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
        description="Test description",
        terms_of_service="https://www.sds.com/policies/terms/",
        contact=openapi.Contact(email="contact@sds.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    # path('', views.home,name='home'),
      #    path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),

    #staff Urls
    path('signup/staff/', StaffSignUpView.as_view()),
    path('signup/student/', StudentSignUpView.as_view()),
    path('api/profile/', views.profile.as_view(),name='profile'),
    path('api/update_profile/', views.UpdateProfile.as_view(), name='profile_update'),
    path('staff/create_categories/',views.categoryCreation, name="category"),
    path('staff/add_post/', views.PostList.as_view(), name='staffpostendpoint'),
    path('staff/post/<int:pk>/', views.SinglePostList.as_view(), name='singlepost'),
    path('staff/post/<int:pk>/comment/', views.PostComment.as_view(), name='comment'),
    path('posts/<int:pk>/like/',views.LikesView.as_view(),name = 'post_likes'),
    
    
    
    #Admin Urls
    path('admin/post/<int:pk>/', views.SinglePostList.as_view(), name='singlepost'),
    path('admin/add_users/', views.AddUser.as_view(), name='singlepost'),
    
    
]
