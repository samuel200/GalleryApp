from django import forms
from showcase import models

class PhotoPost(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = ['image', 'title', 'description']
