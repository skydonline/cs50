from django.contrib import admin
from .models import User,Post,Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")

class PostAdmin(admin.ModelAdmin):
    list_display = ("user",)

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user","post")

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)