from django.contrib import admin

from .models import User, Category, Listing, Bid, Comment

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "first_name", "last_name", "email")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

class ListingAdmin(admin.ModelAdmin):
    list_display = ("title","seller","og_price", "price","category", "date", "for_sale", "winner")

class BidAdmin(admin.ModelAdmin):
    list_display = ("user","amount","date", "listing")

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user","comment","date", "listing")

admin.site.register(User, UserAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Listing, ListingAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment, CommentAdmin)