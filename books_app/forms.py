from django import forms
from .models import Books

class BookCreationForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=['title', 'author', 'summary']
