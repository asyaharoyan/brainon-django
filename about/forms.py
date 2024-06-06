from django import forms
from .models import CollaborateRequest

class CollaborateForm(forms.ModelForm):
    """
    Form for teachers to send collaboration request
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')
