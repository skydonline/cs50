from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Category, Listing, Bid, Comment


def index(request):
    listings = Listing.objects.all()
    return render(request, "auctions/index.html", {
        'listings':listings,
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create_listing(request):
    if request.method == 'POST':
        title = request.POST['title']
        details = request.POST['details']
        price = request.POST['price']
        imageURL = request.POST['imageURL']
        category = request.POST['category']
        user = request.user

        categoryName = Category.objects.get(name=category)

        newListing = Listing(
            title = title,
            details=details,
            price=price,
            imageURL=imageURL,
            seller=user,
            category=categoryName
        )
        newListing.save()

        return redirect('index')
    categories = Category.objects.all()
    return render(request, "auctions/create.html", {
        'categories':categories
        })

def listing(request, id, bid_success='None'):
    listing = Listing.objects.get(pk=id)
    user = request.user
    comments = Comment.objects.filter(listing=id)
    if user.is_authenticated:
        user_watchlist = user.watchlist.values_list('id', flat=True)
    else:
        user_watchlist = None

    return render(request, 'auctions/listing.html', {
        'id': listing.id,
        'title': listing.title,
        'details': listing.details,
        'price': listing.price,
        'category': listing.category,
        'imageURL': listing.imageURL,
        'user_watchlist': user_watchlist,
        'bid_success': bid_success,
        'seller':listing.seller,
        'comments':comments,
        'for_sale':listing.for_sale,
        'winner': listing.winner
    })

def watchlist(request):
    if request.method == 'POST':
        user = request.user
        id = request.POST['id']
        item = Listing.objects.get(pk=id)
        if item in user.watchlist.all():
            user.watchlist.remove(item)
            user.save()
        else:
            user.watchlist.add(item)
            user.save()

        user_watchlist = user.watchlist.all()
        return render(request, 'auctions/watchlist.html', {
            'watchlist':user_watchlist
        })
    user = request.user
    user_watchlist = user.watchlist.all()
    return render(request, 'auctions/watchlist.html', {
        'watchlist':user_watchlist
    })

def bid(request, id):
    bid_amount = request.POST['bid_amount']
    listing = Listing.objects.get(pk=id)
    if float(bid_amount) > listing.price:
        listing.price = bid_amount
        listing.winner = request.user
        listing.save()
        bid_success = True
    else:
        bid_success = False
    return redirect('bid_success', id=id, bid_success=bid_success)

def close(request, id):
    listing = Listing.objects.get(pk=id)
    listing.for_sale = False
    listing.save()
    return redirect('listing', id=id)

def comment(request, id):
    listing = Listing.objects.get(pk=id)
    comment = request.POST['comment']
    comment_content = Comment(user=request.user, comment=comment, listing=listing)
    comment_content.save()
    return redirect('listing', id=id)

def categories(request):
    return render(request, 'auctions/categories.html', {
        'categories':Category.objects.all()
    })

def category_page(request, id):
    listings = Listing.objects.filter(category=id)
    return render(request, 'auctions/category_page.html', {
        'id':id,
        'category': Category.objects.get(pk=id),
        'listings':listings
    })