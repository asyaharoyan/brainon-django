from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    """
    Form for users to comment a lesson
    """
    class Meta:
        model = Comment
        fields = ('body',)