# snippets/forms.py
from django import forms
from .models import Snippet

class SnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'code', 'language', 'public']
        widgets = {
            'code': forms.Textarea(attrs={'rows': 10}),
        }