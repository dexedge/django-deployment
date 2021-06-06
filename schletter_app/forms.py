from django import forms
from .models import Author, Composer
from ckeditor.widgets import CKEditorWidget


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