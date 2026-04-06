from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Write your comment here...'}),
        }
