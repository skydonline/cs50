from django.forms import ModelForm
from .models import *

class UserProfilePic(ModelForm):
    class Meta:
        model = User
        fields = ['profilePic']

class PostImage(ModelForm):
    class Meta:
        model = Post
        fields = ['image']