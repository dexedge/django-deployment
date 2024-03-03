from django import forms
from .models import Event, Work, Author, Composer 
from ckeditor.widgets import CKEditorWidget

class EventForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Event
        fields = ['theater', 'company', 'title', 'notes']
        THEATER_CHOICES = (
            ('Bth', 'Bth'),
            ('Kth', 'Kth')
        )
        COMPANY_CHOICES = (
            ('Court', 'Court'),
            ('French', 'French'),
            ('Jahn', 'Jahn'),
            ('Kinder', 'Kinder'),
            ('Preßburg', 'Preßburg'),
            ('unknown', 'unknown'),
        )
        widgets = {
            'theater': forms.Select(choices=THEATER_CHOICES, attrs={'class': 'form-control'}),
            'company': forms.Select(choices=COMPANY_CHOICES, attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WorkForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Work
        fields = ['title', 'notes', 'url', 'title_page']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'title_page': forms.ClearableFileInput(),
        }

class AuthorForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Author
        fields = ['birth', 'death', 'notes']
        widgets = {
            'birth': forms.NumberInput(attrs={'class': 'form-control'}),
            'death': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ComposerForm(forms.ModelForm):
    notes = forms.CharField(widget=CKEditorWidget(), required=False)

    class Meta:
        model = Composer
        fields = ['birth', 'death', 'notes']
        widgets = {
            'birth': forms.NumberInput(attrs={'class': 'form-control'}),
            'death': forms.NumberInput(attrs={'class': 'form-control'}),
        }