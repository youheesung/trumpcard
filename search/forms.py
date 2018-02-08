from .models import (
    Play,
    Review
    )
from django import forms
from django_summernote.widgets import SummernoteWidget


class PlayForm(forms.ModelForm):
    class Meta:
        model = Play
        fields = '__all__'


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'content']
        widgets = {
            'content': SummernoteWidget(),
          }
