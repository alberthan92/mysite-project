from django import forms

__all__ = [
    'PhotoForm',
]

class PhotoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    description = forms.CharField(
        max_length=80,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
        })
    )
    img = forms.ImageField(required=True)