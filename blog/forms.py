from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Images


class UploadImages(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["image", "description"]

class EditImageForm(forms.ModelForm):
    class Meta:
        model = Images
        fields = ["image", "description"]
