from django.contrib import admin
from .models import User, Email

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")

class EmailAdmin(admin.ModelAdmin):
    list_display = ("user", "sender")

admin.site.register(User, UserAdmin)
admin.site.register(Email, EmailAdmin)