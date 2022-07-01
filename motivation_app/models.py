from django.db import models

from django.core.validators import FileExtensionValidator

from django.contrib.auth.models import AbstractUser
from django.forms import ImageField

class User(AbstractUser):
    is_admin = models.BooleanField('Is admin', default=False)
    is_staff = models.BooleanField('Is staff', default=False)
    is_student = models.BooleanField('Is student', default=False)
    
    
class Profile(models.Model):
    user_id=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    firstname=models.CharField(max_length=100,blank=True,null=True)
    lastname=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='images_uploaded', null=True)
    bio=models.TextField(blank=True,null=True)
    
    
    

class Category(models.Model):
    type= models.CharField(max_length=100, null=True)

class Post(models.Model):
    content_name=models.CharField(max_length=100,null=True,blank=True)
    content_image=models.ImageField(null=True,upload_to='images_uploaded')
    video = models.FileField(null=True,upload_to='videos_uploaded',
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField(null=False)
    date_posted=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    comments = models.ManyToManyField('Comment', null=True)
    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
        
    def update_post(self):
        self.update()
    
    
    def __str__(self):
        return self.content_name

class Comment(models.Model):
    comment= models.TextField(null=True, blank=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    child_comment=models.ManyToManyField('Comment', related_name='comment_child_comment', null=True)
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

class Likes(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    post_id= models.ForeignKey(Post,on_delete=models.CASCADE)
    
    
    def save_likes(self):
        self.save()

    def delete_likes(self):
        self.delete()
        
        
    def update_likes(self):
        self.update()
        
    



class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
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
    
    

#Models
# User
# Posts/content
# Profile
# Comments
# Likes
# Categories
# Dislikes
# wishlist