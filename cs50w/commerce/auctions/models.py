from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    watchlist = models.ManyToManyField('Listing', related_name='watching', blank=True)

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Listing(models.Model):
    title = models.CharField(max_length=30)
    details = models.CharField(max_length=300)
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='listings')
    og_price = models.FloatField(max_length=10)
    price = models.FloatField(max_length=10)
    imageURL = models.CharField(max_length=100, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='listings', blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    for_sale = models.BooleanField(default=True)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner", blank=True, null=True)

    def __str__(self):
        return self.title

class Bid(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bidder")
    amount = models.FloatField(max_length=10)
    date = models.DateField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_bid")

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter")
    comment = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comment")