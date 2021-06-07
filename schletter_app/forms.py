from django import forms
from .models import Author, Composer, Work
from ckeditor.widgets import CKEditorWidget


class WorkForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Work
        fields = ['title', 'notes', 'url']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
        }

class AuthorForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Author
        fields = ['birth', 'death', 'notes']
        widgets = {
            'birth': forms.NumberInput(attrs={'class': 'form-control'}),
            'death': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ComposerForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Composer
        fields = ['birth', 'death', 'notes']
        widgets = {
            'birth': forms.NumberInput(attrs={'class': 'form-control'}),
            'death': forms.NumberInput(attrs={'class': 'form-control'}),
        }