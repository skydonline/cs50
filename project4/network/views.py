from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
import json

from .models import User, Post, Comment


def index(request):
    posts = Post.objects.all().order_by('-date')
    all_posts_api(request)
    return render(request, "network/index.html", {
        'post':posts
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
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


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
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")
    

def settings(request):
    user = request.user
    return render(request, 'network/settings.html', {
        'user':user
    })

def change_password(request):
    user = request.user
    return render(request, 'network/change_password.html')

@csrf_exempt
def password(request, userID):
    if request.method == 'PUT':
        data = json.loads(request.body)
        new_password = data.get('new_password')
        user = User.objects.get(pk=userID)
        user.set_password(new_password)
        user.save()
        message = "Password successfully updated."
        return JsonResponse({"message": message})
    else:
        message = "Unauthorized."
        return JsonResponse({"message": message})

@csrf_exempt
def settings_api(request, userID):
    if request.method == 'PUT':
        data = json.loads(request.body)
        username = data.get('username')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        user = User.objects.get(pk=userID)

        user.username = username
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()
        message = "User settings successfully updated."
        return JsonResponse({"message": message})
    else:
        message = "Unauthorized."
        return JsonResponse({"message": message})
    

def all_posts_api(request):
    current = request.GET.get('current', 0)
    step = request.GET.get('step', 10)
    current = int(current)
    step = int(step)
    posts = Post.objects.order_by('-date')[current:current + step]
    data = {
        'posts': [
            {
                'id': post.id,
                'user': post.user.username,
                'userID': post.user.id,
                'content': post.content,
                'likes': post.likes.count(),
                'date': post.get_formatted_date(),
            }
            for post in posts
        ]
    }
    return JsonResponse(data)


@csrf_exempt
def post_api(request, postID):
    try:
        post = Post.objects.get(id=postID)
    except Post.DoesNotExist:
        return JsonResponse({"Error: Post was not found."}, status=404)

    # updates current post
    if request.method == "PUT":
        data = json.loads(request.body)
        new_content = data.get("content")

        if new_content:
            post.content = new_content
            post.save()

            response_data = {
                "id": post.id,
                "user": post.user.username,
                "content": post.content,
                "likes": post.likes,
                "date": post.get_formatted_date(),
            }

            return JsonResponse(response_data)

    return JsonResponse({"Error: Invalid request"}, status=400)


def new_post(request):
    if request.method == 'POST':
        user = request.user
        content = request.POST['new_post_text']
        new_post = Post(user=user, content=content)
        new_post.save()
        return redirect('index')
    return render(request, 'network/newpost.html')


def profile(request, user_profile):
    user = request.user
    posts = Post.objects.filter(user=user_profile).order_by('-date')
    userID = User.objects.get(id=user_profile)
    posts_count = len(posts)
    following_count = userID.following.count()
    followers_count = userID.followers.count()
    if user in userID.following.all():
        is_following = True
    else:
        is_following = False
    return render(request, 'network/profile.html', {
        'user':user,
        'user_profile':userID,
        'posts':posts,
        'posts_count':posts_count,
        'following_count':following_count,
        'followers_count':followers_count,
        'is_following':is_following
    })

@csrf_exempt
def followers(request, profile):
    user = User.objects.get(id=profile)
    
    # gets followers
    if request.method == 'GET':
        followers = user.followers.all()    
        data = {
            'followers': [follower.username for follower in followers]
        }
        return JsonResponse(data)
            
@csrf_exempt
def following(request, profile):
    user = User.objects.get(id=profile)

    if request.method == 'GET':
        followings = user.following.all()    
        data = {
            'following': [following.username for following in followings]
        }
        return JsonResponse(data)
    
    # adds or removes followers
    elif request.method == 'PUT':
        data = json.loads(request.body)
        user_change = data.get('following')
        userID_change = User.objects.get(username=user_change)
        action = data.get('action')

        if action == 'add':
            user.following.add(userID_change)

        elif action == 'remove':
            user.following.remove(userID_change)

        user.save()
        return JsonResponse('Successfully updated followers.', safe=False)


def following_posts(request):
    user = request.user
    user_following = user.following.all()
    posts = Post.objects.filter(user__in=user_following)
    return render(request, 'network/following.html', {
        'posts':posts
    })

@csrf_exempt
def post_likes(request, postID):
    post = Post.objects.get(id=postID)

    if request.method == 'GET':
        likes_users = post.likes.all()
        data = {
            'usersid': [user.id for user in likes_users]
        }
        return JsonResponse(data)
    
    elif request.method == 'PUT':
        data = json.loads(request.body)
        user = data.get('user')
        action = data.get('action')

        if action == 'add':
            post.likes.add(user)

        elif action == 'remove':
            post.likes.remove(user)

        post.save()
        return JsonResponse('Successfully updated likes.', safe=False)