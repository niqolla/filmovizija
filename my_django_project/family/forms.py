from django import forms
from .models import Post, Comment, Suggestion

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': "What's on your mind?"}),
            'image': forms.FileInput(attrs={'class': 'form-control'})
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 1, 'placeholder': 'Write a comment...'})
        }

class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ['title', 'description']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Suggestion Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Describe your suggestion...'})
        }
