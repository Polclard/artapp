from django import forms
from .models import *


class ArtForm(forms.ModelForm):
    class Meta:
        model = Art
        exclude = ['artist', 'exhibition']
        widgets = {
            'creation_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def __init__(self, *args, **kwargs):
        super(ArtForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            if visible.name == 'is_open':
                visible.field.widget.attrs["class"] = "form-check-input"
