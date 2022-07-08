from django.db import models

from django.core.validators import FileExtensionValidator

from django.contrib.auth.models import AbstractUser
from django.forms import ImageField
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_student = models.BooleanField('Is student', default=False)
    
    def __str__(self):
        return self.username
    
    
#using signals to create authentication token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        

class Admin(models.Model):
    user=models.OneToOneField(User ,related_name='admin',on_delete=models.CASCADE)
    username=models.CharField(max_length=100, null=True)
    phone_number=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.user.username
    
class Staff(models.Model):
    user=models.OneToOneField(User ,related_name='staff',on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return self.user.username
    
    
class Student(models.Model):
    user=models.OneToOneField(User ,related_name='student',null=True, on_delete=models.CASCADE)
    reg_no=models.CharField(max_length=200, null=True)
    course=models.CharField(max_length=200,null=True)
    posts=models.ForeignKey('Post', null=True,blank=True ,on_delete=models.CASCADE)
    comments=models.ForeignKey('Comment', null=True,blank=True ,on_delete=models.CASCADE)
    categories=models.ForeignKey('Category', null=True,blank=True ,on_delete=models.CASCADE)
    wished_item=models.ForeignKey('Wishlist',null=True,blank=True ,on_delete=models.CASCADE)

    def save_student(self):
        self.save()

    def delete_student(self):
        self.delete()
        
        
    def update_student(self):
        self.update()

    def __str__(self):
        return self.user.username
    
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    firstname=models.CharField(max_length=100,blank=True,null=True)
    lastname=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='images_uploaded', null=True)
    bio=models.TextField(blank=True,null=True)
    
    # def __str__(self):
    #     return self.user.firstname
    
    #Signals for saving profile when a user is created
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
        
        
    def save_profile(self):
        self.save()
    
    
    

class Category(models.Model):
    user = models.ForeignKey(User, related_name="cat", blank=True, null=True, on_delete=models.CASCADE)
    type= models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.type

class Post(models.Model):
    content_name=models.CharField(max_length=100,null=True,blank=True)
    content_image=models.ImageField(null=True,blank=True,upload_to='images_uploaded')
    video = models.FileField(null=True,blank=True,upload_to='videos_uploaded',
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    comments = models.ManyToManyField('Comment', null=True,blank=True)
    
    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
        
    def update_post(self):
        self.update()
    
    
    def __str__(self):
        return self.description

class Comment(models.Model):
    comment= models.TextField(null=True, blank=True)
    # parent_comment= models.ForeignKey("self", null=True, blank=True,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True )
    post_id=models.ForeignKey(Post, on_delete= models.CASCADE,null=True, blank=True)
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
        
    def update_comment(self):
        self.update()
        
    def __str__(self):
        return self.comment
    
    
class ChildComment(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True )
    comment_id =models.ForeignKey(Comment, null=True, blank=True,on_delete=models.CASCADE)
    child_comment=models.TextField(null=True)
    date_commented=models.DateTimeField(auto_now_add=True, null=True)
    
    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
        
        
    def update_comment(self):
        self.update()
        
    def __str__(self):
        return self.comment
    
    



class Likes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    post_id= models.ForeignKey(Post,on_delete=models.CASCADE, null=True)
    
    
    def save_likes(self):
        self.save()

    def delete_likes(self):
        self.delete()
        
        
    def update_likes(self):
        self.update()
        
    



class Wishlist(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE,null=True)
    wished_item = models.ForeignKey(Post,on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def save_wish_item(self):
        self.save()

    def delete_wish_item(self):
        self.delete()
        
        
    def update_wish_item(self):
        self.update()
    

class Subscription(models.Model):
    email = models.EmailField(null=True)
    category_id=models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    
    def save_subscription(self):
        self.save()

    def delete_subscription(self):
        self.delete()
        
        
    def update_subscription(self):
        self.update()
        
        
    def __str__(self):
        return self.email
    
# class Addedusers(models.Model):
#     firstname= models.CharField(max_length=50, null=True)
#     lastname= models.CharField(max_length=50, null=True)
#     username= models.CharField(max_length=50, null=True)
#     role = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    

#Models
# User
# Posts/content
# Profile
# Comments
# Likes
# Categories
# Dislikes
# wishlist
#Added Users
