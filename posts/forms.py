from django import forms
from .models import Post



class Postform(forms.ModelForm):
    class Meta():
        model=Post
        #fields='__all__'
        #fields=['title','active','image','contnent']
        exclude=['author','file']