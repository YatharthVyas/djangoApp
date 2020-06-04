from django import forms
from .models import *
from django.contrib.auth.models import User as djangoUser
from django.contrib.auth.forms import UserCreationForm

class CreatePostForm(forms.ModelForm):
	title= forms.CharField(widget=forms.TextInput(
		attrs={
			'class':'form-control',
		}	
	))
	class Meta:
		model = Post
		fields = '__all__' #['Title','Content']
		widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CreateUserForm(UserCreationForm):
	class Meta:
		model = djangoUser
		fields = ['username','first_name','last_name','email','password1','password2']


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = '__all__'
		widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }