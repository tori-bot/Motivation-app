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


class Role(models.Model):
    
    
    name = models.CharField(
        max_length=30, null=True
    )
    
    def insert_roles(self):
        roles = ["ADMIN", "STAFF", "STUDENT"]
        for role in roles:
            new_role = Role(name=role)
            new_role.save()

    def __str__(self):
        return self.name



class User(AbstractUser):
    ADMIN=1
    STAFF=2
    STUDENT=3
    
    ROLES = (
        (ADMIN, "Admin"),
        (STAFF, "Staff"),
        (STUDENT, "Student"),
    )
    
    role = models.PositiveSmallIntegerField(choices=ROLES,null=True)

    def __str__(self):
        return f"{self.username} - {self.get_role_display()}"

    # is_admin = models.BooleanField('Is admin', default=False)
    # is_staff = models.BooleanField('Is staff', default=False)
    # is_student = models.BooleanField('Is student', default=False)
    
    # def __str__(self):
    #     return self.username
    
    
    
#using signals to create authentication token
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
        
ROLES = (
    ('Admin', 'Admin'),
    ('Staff', 'Staff'),
    ('Student', 'Student'),
)
        

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
    subscriptions=models.ForeignKey('Subscription',null=True,blank=True,on_delete=models.CASCADE)

    def save_student(self):
        self.save()

    def delete_student(self):
        self.delete()
        
        
    def update_student(self):
        self.update()

    def __str__(self):
        return self.user.username
    

# def upload_path(instance, filename):
#     return '/'.join(['profile_pics', str(instance.title), filename])

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    firstname=models.CharField(max_length=100,blank=True,null=True)
    lastname=models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    profile_pic=models.ImageField(upload_to='upload_path', null=True)
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


# def upload_path(instance, filename):
#     return '/'.join(['content_images', str(instance.content_name), filename])
# def upload_to(instance, filename):
#     return 'images/{filename}'.format(filename=filename)

class Post(models.Model):
    content_name=models.CharField(max_length=100,null=True,blank=True)
    content_image=models.FileField(null=True,blank=True,upload_to='images_uploaded')
    video = models.FileField(null=True,blank=True,upload_to='videos_uploaded',
    validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField()
    date_posted=models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True,blank=True)
    comments = models.ForeignKey('Comment',on_delete=models.CASCADE, null=True,blank=True)
    
    
    
    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
        
        
    def update_post(self):
        self.update()
    
    
    def __str__(self):
        return self.content_name

class Comment(models.Model):
    post_id=models.ForeignKey(Post, on_delete= models.CASCADE,null=True, blank=True)
    comment= models.TextField(null=True, blank=True)
    date_posted=models.DateTimeField(auto_now_add=True)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE, null=True )
    
    
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
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    
    def save_subscription(self):
        self.save()

    def delete_subscription(self):
        self.delete()
        
        
    def update_subscription(self):
        self.update()
        
        
    def __str__(self):
        return self.email
    

# class ImageUpload(models.Model):
#     file =models.ImageField(null=True,blank=True,upload_to='images_uploaded')

#     def __str__(self):
#         return self.file


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
