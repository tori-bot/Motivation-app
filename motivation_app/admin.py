from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Admin)
admin.site.register(Staff)
admin.site.register(Student)
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Likes)
admin.site.register(Comment)
admin.site.register(Wishlist)
